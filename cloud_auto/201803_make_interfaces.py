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
if not os.path.exists(current_path+"/interfaces/"):
	os.makedirs(current_path+"/interfaces/",exist_ok=True)

def gen_netplan(host_info):
	h_name=host_info.host_name
	template="""# This file describes the network interfaces available on your system
# For more information, see netplan(5).
network:
  version: 2
  renderer: networkd
  ethernets:
    {vlan_raw_device}:
      dhcp4: no
      dhcp6: no
    eno2:
      dhcp4: no
      dhcp6: no
      addresses: [{eno2_ip}/{eno2_netmask}]
  vlans:
    eno1.2:
      id: 2
      link: {vlan_raw_device}
      dhcp4: no
      dhcp6: no
      addresses: [{eno1_2_ip}/{eno1_2_netmask}]
      gateway4: {gateway}
    eno1.3:
      id: 3
      link: {vlan_raw_device}
      dhcp4: no
      dhcp6: no
      addresses: [{eno1_3_ip}/{eno1_3_netmask}]
"""
	shell_template="""#!/bin/bash
for dir in /etc/netplan/*;
do
    org_netplan=$dir;
    base_org_netplan=$(basename "$org_netplan")
    if [ -f "/root/$base_org_netplan" ];
    then
        echo "original netplan file exists"
    else
        ## copy original netplan file to root
        cp $org_netplan /root/
    fi
done

## copy generate netplan to /etc/netplan
cp /root/gen* $org_netplan

netplan apply
sleep 2
ip link set dev {vlan_raw_device} address {pseudomac}
ip link set dev eno1.2 address {pseudomac}
ip link set dev eno1.3 address {pseudomac}

sed -i "/^#DNS=/c\DNS=8.8.8.8" /etc/systemd/resolved.conf
systemctl restart systemd-resolved
"""
	if host_info.ifaceInfo_list[2].netmask == "255.255.0.0":
		_eno2_netmask=16
	else:
		print("there is no eno2 netmask")
	if host_info.ifaceInfo_list[1].netmask == "255.255.192.0" and host_info.ifaceInfo_list[0].netmask == "255.255.192.0":
		_eno1_netmask=18
	else:
		print("there is no eno1.2 eno1.3 netmask")
	if host_info.ifaceInfo_list[1].netmask == "255.255.255.0" and host_info.ifaceInfo_list[0].netmask == "255.255.255.0":
		_eno1_netmask=24
	else:
		print("there is no v-12345678 bridges")

	with open('./interfaces/gen_01-netcfg_'+h_name+'.yaml','w') as gen_file:
		gen_file.write(template.format(vlan_raw_device=host_info.ifaceInfo_list[0].vlan_raw_dev, eno2_ip=host_info.ifaceInfo_list[2].ipv4,
			eno2_netmask=_eno2_netmask, eno1_2_ip=host_info.ifaceInfo_list[0].ipv4, 
			eno1_2_netmask=_eno1_netmask, gateway=host_info.ifaceInfo_list[0].gateway, 
			eno1_3_ip=host_info.ifaceInfo_list[1].ipv4, eno1_3_netmask=_eno1_netmask))
	with open('./interfaces/net_setting_apply_link_pseudomac_'+h_name+'.sh','w') as gen_shell:
		gen_shell.write(shell_template.format(vlan_raw_device=host_info.ifaceInfo_list[0].vlan_raw_dev, pseudomac=host_info.ifaceInfo_list[0].pseudomac))
	os.system("scp "+current_path+"/interfaces/gen_01-netcfg_"+h_name+".yaml"+" root@"+host_info.ifaceInfo_list[2].ipv4+":/root/")
	os.system("scp "+current_path+"/interfaces/net_setting_apply_link_pseudomac_"+h_name+".sh"+" root@"+host_info.ifaceInfo_list[2].ipv4+":/root/")
	os.system("ssh root@"+host_info.ifaceInfo_list[2].ipv4+" 'chmod 755 /root/net_setting_apply_link_pseudomac_"+h_name+".sh'")
	os.system("ssh root@"+host_info.ifaceInfo_list[2].ipv4+" './net_setting_apply_link_pseudomac_"+h_name+".sh'")
	os.system("echo 'ip link set eno1 address "+host_info.ifaceInfo_list[0].pseudomac+"' | ssh root@"+host_info.ifaceInfo_list[2].ipv4+" 'cat >> /etc/profile'")

def all_host_interfaces(version):
	if(version=="Ubuntu 16.04.3 LTS"):
		host_info_list=host.InfoList("./config/host_info")
		
		for host_info in host_info_list.HostInfo_list:
			h_name=host_info.host_name
			shutil.copy(current_path+"/interfaces_initial", current_path+"/interfaces/interfaces"+h_name)
			with open(current_path+"/interfaces/interfaces"+h_name, 'r+') as f:
				host_info=host_info_list.get_host(h_name)
				lines=[]
				new_line='\n'+'auto '+host_info.ifaceInfo_list[0].iface_name+'\n'+'iface '+host_info.ifaceInfo_list[0].iface_name+' inet static\n'+'address '+host_info.ifaceInfo_list[0].ipv4+'\n'+'hwaddress ether '+host_info.ifaceInfo_list[0].pseudomac+'\n'+'netmask '+host_info.ifaceInfo_list[0].netmask+'\n'+'gateway '+host_info.ifaceInfo_list[0].gateway+'\n'+'vlan-raw-device '+host_info.ifaceInfo_list[0].vlan_raw_dev+'\n'+'dns-nameservers '+host_info.ifaceInfo_list[0].dns+'\n'+'\n'+'auto '+host_info.ifaceInfo_list[1].iface_name+'\n'+'iface '+host_info.ifaceInfo_list[1].iface_name+' inet static\n'+'address '+host_info.ifaceInfo_list[1].ipv4+'\n'+'hwaddress ether '+host_info.ifaceInfo_list[1].pseudomac+'\n'+'netmask '+host_info.ifaceInfo_list[1].netmask+'\n'+'vlan-raw-device '+host_info.ifaceInfo_list[1].vlan_raw_dev+'\n'+'\n'+'auto '+host_info.ifaceInfo_list[2].iface_name+'\n'+'iface '+host_info.ifaceInfo_list[2].iface_name+' inet static\n'+'address '+host_info.ifaceInfo_list[2].ipv4+'\n'+'netmask '+host_info.ifaceInfo_list[2].netmask
				for line in f:
					if(line.startswith('iface lo')):
						lines=lines+[new_line]
				f.writelines(lines)
			os.system("scp "+current_path+"/interfaces/interfaces"+h_name+" root@"+host_info.ifaceInfo_list[2].ipv4+":/root/")
	elif(version=="TmaxLinux 4.0"):
		host_info_list=host.InfoList("./config/host_info")
		for host_info in host_info_list.HostInfo_list:
			gen_netplan(host_info)
		
	else:
		print("Check os_version in ./ansible/vars/common_vars.yml file \n We are support Ubuntu 16.04, 17.10 version")
	
def part_host_interfaces(version, host_name):
	host_info_list=host.InfoList("./config/host_info")
	if(version=="Ubuntu 16.04.3 LTS"):
		h_name=host_name
		shutil.copy(current_path+"/interfaces_initial", current_path+"/interfaces/interfaces"+h_name)
		with open(current_path+"/interfaces/interfaces"+h_name, 'r+') as f:
			host_info=host_info_list.get_host(h_name)
			lines=[]
			new_line='\n'+'auto '+host_info.ifaceInfo_list[0].iface_name+'\n'+'iface '+host_info.ifaceInfo_list[0].iface_name+' inet static\n'+'address '+host_info.ifaceInfo_list[0].ipv4+'\n'+'hwaddress ether '+host_info.ifaceInfo_list[0].pseudomac+'\n'+'netmask '+host_info.ifaceInfo_list[0].netmask+'\n'+'gateway '+host_info.ifaceInfo_list[0].gateway+'\n'+'vlan-raw-device '+host_info.ifaceInfo_list[0].vlan_raw_dev+'\n'+'dns-nameservers '+host_info.ifaceInfo_list[0].dns+'\n'+'\n'+'auto '+host_info.ifaceInfo_list[1].iface_name+'\n'+'iface '+host_info.ifaceInfo_list[1].iface_name+' inet static\n'+'address '+host_info.ifaceInfo_list[1].ipv4+'\n'+'hwaddress ether '+host_info.ifaceInfo_list[1].pseudomac+'\n'+'netmask '+host_info.ifaceInfo_list[1].netmask+'\n'+'vlan-raw-device '+host_info.ifaceInfo_list[1].vlan_raw_dev+'\n'+'\n'+'auto '+host_info.ifaceInfo_list[2].iface_name+'\n'+'iface '+host_info.ifaceInfo_list[2].iface_name+' inet static\n'+'address '+host_info.ifaceInfo_list[2].ipv4+'\n'+'netmask '+host_info.ifaceInfo_list[2].netmask
			for line in f:
				if(line.startswith('iface lo')):
					lines=lines+[new_line]
				f.writelines(lines)
		os.system("scp "+current_path+"/interfaces/interfaces"+h_name+" root@"+host_info.ifaceInfo_list[2].ipv4+":/root/")
	elif(version=="TmaxLinux 4.0"):
		host_info_list=host.InfoList("./config/host_info")
		host_info=host_info_list.get_host(host_name)
		gen_netplan(host_info)
	else:
		print("Check os_version in ./ansible/vars/common_vars.yml file \n We are support Ubuntu 16.04, 17.10 version")
		

if __name__ == "__main__":
	os_version_parsing=str(subprocess.check_output('cat /etc/issue.net', shell=True))
	os_version=os_version_parsing.replace('\n','').replace("'","")
	os_version=os_version[1:-2]
	#print(os_version)
	if(len(sys.argv) <=1):
		print("./make_interfaces.py -h or --help will be helpful")
		sys.exit()
	use = """Usage: ./%prog [options] [hostname]
		./%prog -n [hostname]
		./%prog --name [hostname]
		ex) ./%prog -n all 
		ex) ./%prog -n C4-6
	"""
	parser = OptionParser(usage=use)

	help_info ="""Make network interfaces for Host
	It is classified by ubuntu version & all or not. Program ask you that ubuntu version is correct
	[hostname] = all / Host name exists in host_info
	"""
	#parser.add_option("-v","--version",dest="version",default=False, action="store_true", help="Network interfaces for Ubuntu version ex) Ubuntu 16.04.3 LTS / TmaxLinux 4.0")
	parser.add_option("-n","--name", dest="name",default=False, action="store_true", help="Make all network interfaces or specific network interfaces")

	options, args= parser.parse_args()
	f=open("./ansible/vars/common_vars.yml",'r')
	lines=f.readlines()
	#os_version="".join([s.split(":")[-1] for s in lines if 'os_version' in s][0]).replace('\n','').replace(' ','').replace('"','')

	if options.name:
		if(args[0] == "all"):
			all_host_interfaces(os_version)
		else:
			part_host_interfaces(os_version, host_name=args[0])
