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
      id: 3
      link: {vlan_raw_device_1}
      dhcp4: no
      dhcp6: no
      addresses: [{internal_iface_ip}/{internal_iface_netmask}]
    {iface_name_3}:
      id: 4
      link: {vlan_raw_device_1}
      dhcp4: no
      dhcp6: no
      addresses: [{host_frontend_iface_ip}/{host_frontend_iface_netmask}]
    {iface_name_4}:
      id: 5
      link: {vlan_raw_device_1}
      dhcp4: no
      dhcp6: no
    {iface_name_5}:
      id: 6
      link: {vlan_raw_device_1}
      dhcp4: no
      dhcp6: no
  bridges:
    vbr-5:
      interfaces: [{iface_name_4}]
    vbr-6:
      interfaces: [{iface_name_5}]
"""
	template_master_shell="""
#!/bin/bash

ip link add dev 5in type veth peer name 5out
ip link add dev 6in type veth peer name 6out
ip link set 5in master vbr-5
ip link set 6in master vbr-6

ip link set dev 5in up
ip link set dev 5out up
ip link set dev 6in up
ip link set dev 6out up

ip link set dev vbr-5 up
ip link set dev vbr-6 up

ip address add 172.16.0.1/16 dev 5out
ip address add 172.18.0.1/16 dev 6out
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
      id: 3
      link: {vlan_raw_device_1}
      dhcp4: no
      dhcp6: no
      addresses: [{internal_iface_ip}/{internal_iface_netmask}]
    {iface_name_2}:
      id: 4
      link: {vlan_raw_device_1}
      dhcp4: no
      dhcp6: no
      addresses: [{host_frontend_iface_ip}/{host_frontend_iface_netmask}]
      gateway4: {gateway}
    {iface_name_3}:
      id: 5
      link: {vlan_raw_device_1}
      dhcp4: no
      dhcp6: no
    {iface_name_4}:
      id: 6
      link: {vlan_raw_device_1}
      dhcp4: no
      dhcp6: no
  bridges:
    vbr-5:
      interfaces: [{iface_name_3}]
    vbr-6:
      interfaces: [{iface_name_4}]
"""
	template_infra_lb_shell="""
#!/bin/bash
ip link add dev 5in type veth peer name 5out
ip link add dev 6in type veth peer name 6out
ip link set 6in master vbr-6
ip link set 5in master vbr-5

ip link set dev 6in up
ip link set dev 6out up

ip link set dev 5in up
ip link set dev 5out up

ip link set dev vbr-6 up
ip link set dev vbr-5 up

ip address add {management_iface_ip}/16 dev 6out
ip address add 172.16.0.2/16 dev 5out

"""
	template_infra_shell="""
#!/bin/bash

ip link add dev 6in type veth peer name 6out
ip link set 6in master vbr-6

ip link set dev 6in up
ip link set dev 6out up

ip link set dev vbr-5 up
ip link set dev vbr-6 up

ip address add {management_iface_ip}/16 dev 6out
"""

	_public_iface_netmask=0
	_internal_iface_netmask=0
	_host_frontend_iface_netmask=0
	
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

	if host_info.ifaceInfo_list[4].netmask == "255.255.0.0":
		_internal_iface_netmask = 16
	if host_info.ifaceInfo_list[4].netmask == "255.255.192.0":
		_internal_iface_netmask = 18
	if host_info.ifaceInfo_list[4].netmask == "255.255.255.0":
		_internal_iface_netmask = 24
	
	## make generate yaml file
	if h_tag == "Master":
		with open('./interfaces/noSDN_gen_01-netcfg_'+h_name+'.yaml','w') as gen_file:
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

				iface_name_4=host_info.ifaceInfo_list[2].iface_name,
				iface_name_5=host_info.ifaceInfo_list[3].iface_name))
		gen_file.close()

		with open('./interfaces/noSDN-bridge-master-setting.sh','w') as gen_shell:
			gen_shell.write(template_master_shell)
		gen_shell.close()
		os.system("scp "+current_path+"/interfaces/noSDN-bridge-master-setting.sh"+" root@"+host_info.ifaceInfo_list[4].ipv4+":/root/automation/netplan/")
		os.system("scp "+current_path+"/interfaces/noSDN_gen_01-netcfg_"+h_name+".yaml"+" root@"+host_info.ifaceInfo_list[4].ipv4+":/root/automation/netplan/")

	elif h_tag == "Compute": #or h_tag == "Storage":
		with open('./interfaces/noSDN_gen_01-netcfg_'+h_name+'.yaml','w') as gen_file:
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
		with open('./interfaces/noSDN-bridge-'+h_name+'-normal-setting.sh','w') as gen_shell:
			gen_shell.write(template_infra_shell.format(management_iface_ip=host_info.ifaceInfo_list[3].ipv4))
		gen_shell.close()
		os.system("scp "+current_path+"/interfaces/noSDN-bridge-"+h_name+"-normal-setting.sh"+" root@"+host_info.ifaceInfo_list[4].ipv4+":/root/automation/netplan/")
	
		#print(host_info.ifaceInfo_list[0].ipv4)
		os.system("scp "+current_path+"/interfaces/noSDN_gen_01-netcfg_"+h_name+".yaml"+" root@"+host_info.ifaceInfo_list[4].ipv4+":/root/automation/netplan/")

	elif h_tag == "LB":
		with open('./interfaces/noSDN_gen_01-netcfg_'+h_name+'.yaml','w') as gen_file:
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
		
		with open('./interfaces/noSDN-bridge-'+h_name+'-normal-setting.sh','w') as gen_lb_shell:
			gen_lb_shell.write(template_infra_lb_shell.format(management_iface_ip=host_info.ifaceInfo_list[3].ipv4))
		gen_lb_shell.close()
		os.system("scp "+current_path+"/interfaces/noSDN-bridge-"+h_name+"-normal-setting.sh"+" root@"+host_info.ifaceInfo_list[4].ipv4+":/root/automation/netplan/")
		
		os.system("scp "+current_path+"/interfaces/noSDN_gen_01-netcfg_"+h_name+".yaml"+" root@"+host_info.ifaceInfo_list[4].ipv4+":/root/automation/netplan/")

if __name__=="__main__":
	host_info_list=host.InfoList("./config/host_info_lite")
	for host_info in host_info_list.HostInfo_list:
		gen_lite_netplan(host_info)
