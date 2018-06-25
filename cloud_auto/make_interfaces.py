#!/usr/bin/python3
#-*-coding:utf8;-*-

import host
import os
import sys
import utils
import shutil
import yaml
import subprocess
from optparse import OptionParser

current_path=os.path.dirname(os.path.abspath(__file__))
if not os.path.exists(current_path+'/interfaces/'):
	os.makedirs(current_path+'/interfaces/',exist_ok=True)

def gen_lite_netplan(host_info):
	h_name=host_info.host_name
	h_tag=host_info.tag
	_vars_file=open("ansible/vars/common_vars.yml",'r')
	lines=_vars_file.readlines()
	_all_in_infra="".join([s.split(":")[-1] for s in lines if 'all_in_infra' in s][0]).replace('\n','')
	
	template_master="""# This file describes the network interfaces available on your system
# For more information, see netplan(5).
network:
  version: 2
  renderer: networkd
  ethernets:
    {vlan_raw_device_1}:
      dhcp4: no
      dhcp6: no
  vlans:
    {iface_name_1}:
      id: 2
      link: {vlan_raw_device_1}
      dhcp4: no
      dhcp6: no
      addresses: [{public_iface_ip}/{public_iface_netmask}]
      gateway4: {gateway}
    {iface_name_2}:
      id: 4
      link: {vlan_raw_device_1}
      dhcp4: no
      dhcp6: no
      addresses: [{internal_iface_ip}/{internal_iface_netmask}]
    {iface_name_3}:
      id: 5
      link: {vlan_raw_device_1}
      dhcp4: no
      dhcp6: no
      addresses: [{host_frontend_iface_ip}/{host_frontend_iface_netmask}]
    {iface_name_4}:
      id: 7
      link: {vlan_raw_device_1}
      dhcp4: no
      dhcp6: no
  bridges:
    v-05f5e107:
      interfaces: [{iface_name_4}]
"""
	template_master_shell="""
#!/bin/bash

ip link add dev 7in type veth peer name 7out
ip link set 7in master v-05f5e107

ip link set dev 7in up
ip link set dev 7out up

ip link set dev v-05f5e107 up

ip address add {management_iface_ip}/{management_iface_cidr} dev 7out

ifconfig {vlan_raw_device_1} hw ether {pseudomac_host}
ifconfig 7out hw ether {pseudomac_management}
echo 0 >> /proc/sys/net/bridge/bridge-nf-call-iptables
"""
	template_master_profile_shell="""
ifconfig {vlan_raw_device_1} hw ether {pseudomac_host}
"""

	template_lb="""# This file describes the network interfaces available on your system
# For more information, see netplan(5).
network:
  version: 2
  renderer: networkd
  ethernets:
    {vlan_raw_device_1}:
      dhcp4: no
      dhcp6: no
  vlans:
    {iface_name_1}:
      id: 4
      link: {vlan_raw_device_1}
      dhcp4: no
      dhcp6: no
      addresses: [{internal_iface_ip}/{internal_iface_netmask}]
    {iface_name_2}:
      id: 5
      link: {vlan_raw_device_1}
      dhcp4: no
      dhcp6: no
      addresses: [{host_frontend_iface_ip}/{host_frontend_iface_netmask}]
      gateway4: {gateway}
    {iface_name_3}:
      id: 7
      link: {vlan_raw_device_1}
      dhcp4: no
      dhcp6: no
  bridges:
    v-05f5e107:
      interfaces: [{iface_name_3}]
"""
	template_infra_lb_shell="""
#!/bin/bash
ip link add dev 7in type veth peer name 7out
ip link set 7in master v-05f5e107

ip link set dev 7in up
ip link set dev 7out up

ip link set dev v-05f5e107 up

ip address add {management_iface_ip}/{management_iface_cidr} dev 7out

ifconfig {vlan_raw_device_1} hw ether {pseudomac_host}
ifconfig 7out hw ether {pseudomac_management}
"""
	template_infra_lb_profile_shell="""
ifconfig {vlan_raw_device_1} hw ether {pseudomac_host}
"""

	template_infra="""# This file describes the network interfaces available on your system
# For more information, see netplan(5).
network:
  version: 2
  renderer: networkd
  ethernets:
    {vlan_raw_device_1}:
      dhcp4: no
      dhcp6: no
  vlans:
    {iface_name_1}:
      id: 4
      link: {vlan_raw_device_1}
      dhcp4: no
      dhcp6: no
      addresses: [{internal_iface_ip}/{internal_iface_netmask}]
    {iface_name_2}:
      id: 5
      link: {vlan_raw_device_1}
      dhcp4: no
      dhcp6: no
      addresses: [{host_frontend_iface_ip}/{host_frontend_iface_netmask}]
      gateway4: {gateway}
    {iface_name_3}:
      id: 6
      link: {vlan_raw_device_1}
      dhcp4: no
      dhcp6: no
    {iface_name_4}:
      id: 7
      link: {vlan_raw_device_1}
      dhcp4: no
      dhcp6: no
  bridges:
    v-05f5e106:
      interfaces: [{iface_name_3}]
    v-05f5e107:
      interfaces: [{iface_name_4}]
"""

	template_infra_shell="""
#!/bin/bash

ip link add dev 7in type veth peer name 7out
ip link set 7in master v-05f5e107

ip link set dev 7in up
ip link set dev 7out up

ip link set dev v-05f5e106 up
ip link set dev v-05f5e107 up

ip address add {management_iface_ip}/{management_iface_cidr} dev 7out

ifconfig {vlan_raw_device_1} hw ether {pseudomac_host}
ifconfig 7out hw ether {pseudomac_management}
"""
	template_infra_profile_shell="""
ifconfig {vlan_raw_device_1} hw ether {pseudomac_host}
"""

	_public_iface_netmask=0
	_internal_iface_netmask=0
	_host_frontend_iface_netmask=0
	_host_container_iface_netmask=0
	_host_management_iface_netmask=0
	
	if host_info.ifaceInfo_list[0].netmask == "255.255.0.0":
		_host_frontend_iface_netmask = _public_iface_netmask = 16
	if host_info.ifaceInfo_list[0].netmask == "255.255.192.0":
		_host_frontend_iface_netmask = _public_iface_netmask = 18
	if host_info.ifaceInfo_list[0].netmask == "255.255.255.0":
		_host_frontend_iface_netmask = _public_iface_netmask = 24

	if host_info.ifaceInfo_list[1].netmask == "255.255.0.0":
		_host_frontend_iface_netmask = 16
	if host_info.ifaceInfo_list[1].netmask == "255.255.192.0":
		_host_frontend_iface_netmask = 18
	if host_info.ifaceInfo_list[1].netmask == "255.255.255.0":
		_host_frontend_iface_netmask = 24

	if host_info.ifaceInfo_list[2].netmask == "255.254.0.0":
		_host_container_iface_netmask = 15
	if host_info.ifaceInfo_list[2].netmask == "255.255.0.0":
		_host_container_iface_netmask = 16

	if host_info.ifaceInfo_list[3].netmask == "255.254.0.0":
		_host_management_iface_netmask = 15
	if host_info.ifaceInfo_list[3].netmask == "255.255.0.0":
		_host_management_iface_netmask = 16

	if host_info.ifaceInfo_list[4].netmask == "255.255.0.0":
		_internal_iface_netmask = 16
	if host_info.ifaceInfo_list[4].netmask == "255.255.192.0":
		_internal_iface_netmask = 18
	if host_info.ifaceInfo_list[4].netmask == "255.255.255.0":
		_internal_iface_netmask = 24

	## make generate yaml file
	if h_tag == "Master":
		with open('./interfaces/SDN_gen_01-netcfg_'+h_name+'.yaml','w') as gen_file:
			gen_file.write(template_master.format(vlan_raw_device_1=host_info.ifaceInfo_list[0].vlan_raw_dev,
				iface_name_1=host_info.ifaceInfo_list[0].iface_name,
				public_iface_ip=host_info.ifaceInfo_list[0].ipv4,
				public_iface_netmask=_public_iface_netmask, 
				gateway=host_info.ifaceInfo_list[0].gateway, 
				
				iface_name_2=host_info.ifaceInfo_list[4].iface_name,
				internal_iface_ip=host_info.ifaceInfo_list[4].ipv4,
				internal_iface_netmask=_internal_iface_netmask,

				iface_name_3=host_info.ifaceInfo_list[1].iface_name,
				host_frontend_iface_ip=host_info.ifaceInfo_list[1].ipv4,
				host_frontend_iface_netmask=_host_frontend_iface_netmask,

				iface_name_4=host_info.ifaceInfo_list[3].iface_name))
#				iface_name_5=host_info.ifaceInfo_list[4].iface_name))
		gen_file.close()

		with open('./interfaces/SDN-bridge-master-setting.sh','w') as gen_shell:
#			gen_shell.write(template_master_shell.format(container_iface_ip=host_info.ifaceInfo_list[2].ipv4,
			gen_shell.write(template_master_shell.format(management_iface_ip=host_info.ifaceInfo_list[3].ipv4, 
				vlan_raw_device_1=host_info.ifaceInfo_list[0].vlan_raw_dev,
				pseudomac_host=host_info.ifaceInfo_list[0].pseudomac,
				pseudomac_management=host_info.ifaceInfo_list[3].pseudomac,
#				container_iface_cidr=_host_container_iface_netmask,
				management_iface_cidr=_host_management_iface_netmask))
		gen_shell.close()

		with open('./interfaces/profile_pseudomac','w') as gen_profile:
			gen_profile.write(template_master_profile_shell.format(vlan_raw_device_1=host_info.ifaceInfo_list[0].vlan_raw_dev, pseudomac_host=host_info.ifaceInfo_list[0].pseudomac))
		gen_profile.close()

		os.system("scp "+current_path+"/interfaces/SDN-bridge-master-setting.sh"+" root@"+host_info.ifaceInfo_list[4].ipv4+":/root/automation/netplan/")
		os.system("scp "+current_path+"/interfaces/SDN_gen_01-netcfg_"+h_name+".yaml"+" root@"+host_info.ifaceInfo_list[4].ipv4+":/root/automation/netplan/")
		os.system("scp "+current_path+"/interfaces/profile_pseudomac"+" root@"+host_info.ifaceInfo_list[4].ipv4+":/root/automation/netplan/")

	elif h_tag == "Compute" or h_tag == 'Storage':
		with open('./interfaces/SDN_gen_01-netcfg_'+h_name+'.yaml','w') as gen_file:
			gen_file.write(template_infra.format(vlan_raw_device_1=host_info.ifaceInfo_list[0].vlan_raw_dev,
				iface_name_1=host_info.ifaceInfo_list[4].iface_name,
				internal_iface_ip=host_info.ifaceInfo_list[4].ipv4,
				internal_iface_netmask=_internal_iface_netmask,

				iface_name_2=host_info.ifaceInfo_list[0].iface_name,
				host_frontend_iface_ip=host_info.ifaceInfo_list[0].ipv4,
				host_frontend_iface_netmask=_host_frontend_iface_netmask,
				gateway=host_info.ifaceInfo_list[0].gateway,

				iface_name_3=host_info.ifaceInfo_list[2].iface_name,
				iface_name_4=host_info.ifaceInfo_list[3].iface_name))
		gen_file.close()
		with open('./interfaces/SDN-bridge-'+h_name+'-normal-setting.sh','w') as gen_shell:
			gen_shell.write(template_infra_shell.format(management_iface_ip=host_info.ifaceInfo_list[3].ipv4,
				vlan_raw_device_1=host_info.ifaceInfo_list[0].vlan_raw_dev,
				pseudomac_host=host_info.ifaceInfo_list[0].pseudomac,
				pseudomac_management=host_info.ifaceInfo_list[3].pseudomac,
				management_iface_cidr=_host_management_iface_netmask))
		gen_shell.close()

		with open('./interfaces/profile_pseudomac','w') as gen_profile:
			gen_profile.write(template_master_profile_shell.format(vlan_raw_device_1=host_info.ifaceInfo_list[0].vlan_raw_dev, pseudomac_host=host_info.ifaceInfo_list[0].pseudomac))
		gen_profile.close()


		os.system("scp "+current_path+"/interfaces/SDN-bridge-"+h_name+"-normal-setting.sh"+" root@"+host_info.ifaceInfo_list[4].ipv4+":/root/automation/netplan/")
	
		os.system("scp "+current_path+"/interfaces/SDN_gen_01-netcfg_"+h_name+".yaml"+" root@"+host_info.ifaceInfo_list[4].ipv4+":/root/automation/netplan/")

		os.system("scp "+current_path+"/interfaces/profile_pseudomac"+" root@"+host_info.ifaceInfo_list[4].ipv4+":/root/automation/netplan/")

	elif h_tag == "LB":
		with open('./interfaces/SDN_gen_01-netcfg_'+h_name+'.yaml','w') as gen_file:
			gen_file.write(template_lb.format(vlan_raw_device_1=host_info.ifaceInfo_list[0].vlan_raw_dev,
				iface_name_1=host_info.ifaceInfo_list[4].iface_name,
				internal_iface_ip=host_info.ifaceInfo_list[4].ipv4,
				internal_iface_netmask=_internal_iface_netmask,

				iface_name_2=host_info.ifaceInfo_list[0].iface_name,
				host_frontend_iface_ip=host_info.ifaceInfo_list[0].ipv4,
				host_frontend_iface_netmask=_host_frontend_iface_netmask,
				gateway=host_info.ifaceInfo_list[0].gateway,

				iface_name_3=host_info.ifaceInfo_list[3].iface_name))
#				iface_name_4=host_info.ifaceInfo_list[3].iface_name))
		gen_file.close()
		print(_host_container_iface_netmask)
		with open('./interfaces/SDN-bridge-'+h_name+'-normal-setting.sh','w') as gen_lb_shell:
			gen_lb_shell.write(template_infra_lb_shell.format(management_iface_ip=host_info.ifaceInfo_list[3].ipv4,
#				container_iface_ip=host_info.ifaceInfo_list[2].ipv4,
				vlan_raw_device_1=host_info.ifaceInfo_list[0].vlan_raw_dev,
				pseudomac_host=host_info.ifaceInfo_list[0].pseudomac,
				pseudomac_management=host_info.ifaceInfo_list[3].pseudomac,
#				container_iface_cidr=_host_container_iface_netmask,
				management_iface_cidr=_host_management_iface_netmask))
		gen_lb_shell.close()

		with open('./interfaces/profile_pseudomac','w') as gen_profile:
			gen_profile.write(template_master_profile_shell.format(vlan_raw_device_1=host_info.ifaceInfo_list[0].vlan_raw_dev, pseudomac_host=host_info.ifaceInfo_list[0].pseudomac))
		gen_profile.close()
	
		os.system("scp "+current_path+"/interfaces/SDN-bridge-"+h_name+"-normal-setting.sh"+" root@"+host_info.ifaceInfo_list[4].ipv4+":/root/automation/netplan/")
		
		os.system("scp "+current_path+"/interfaces/SDN_gen_01-netcfg_"+h_name+".yaml"+" root@"+host_info.ifaceInfo_list[4].ipv4+":/root/automation/netplan/")

		os.system("scp "+current_path+"/interfaces/profile_pseudomac"+" root@"+host_info.ifaceInfo_list[4].ipv4+":/root/automation/netplan/")

if __name__=="__main__":
	host_info_list=host.InfoList("./config/host_info")
	for host_info in host_info_list.HostInfo_list:
		gen_lite_netplan(host_info)
