#!/usr/bin/python3
#-*-cdoing:utf8;-*-

import host
import os, sys, utils
import shutil

def all_host_interfaces_clean():
	host_info_list=host.InfoList("./config/host_info")
	for host_info in host_info_list.HostInfo_list:
		h_name=host_info.host_name
		current_path=os.path.dirname(os.path.abspath( __file__ ))
		shutil.copy(current_path+"/interfaces_initial", current_path+"/interfaces/interfaces"+h_name)
		with open(current_path+"/interfaces/interfaces"+h_name, "r+") as f:
			host_info=host_info_list.get_host(h_name)
			lines=[]
			new_line='\n'+'auto '+host_info.ifaceInfo_list[2].iface_name+'\n'+'iface '+host_info.ifaceInfo_list[2].iface_name+' inet static\n'+'address '+host_info.ifaceInfo_list[2].ipv4+'\n'+'netmask '+host_info.ifaceInfo_list[2].netmask
			for line in f:
				if(line.startswith('iface lo')):
					lines=lines+[new_line]
			f.writelines(lines)
		os.system("scp "+current_path+"/interfaces/interfaces"+h_name+" root@"+host_info.ifaceInfo_list[2].ipv4+":/root/")

def part_host_interfaces_clean(host_name):
	host_info_list=host.InfoList("./config/host_info")
	h_name=host_name
	shutil.copy(current_path+"/interfaces_initial", current_path+"/interfaces/interfaces"+h_name)
	with open(current_path+"/interfaces/interfaces"+h_name, "r+") as f:
		host_info=host_info_list.get_host(h_name)
		current_path=os.path.dirname(os.path.abspath( __file__ ))
		lines=[]
		new_line='\n'+'auto '+host_info.ifaceInfo_list[2].iface_name+'\n'+'iface '+host_info.ifaceInfo_list[2].iface_name+' inet static\n'+'address '+host_info.ifaceInfo_list[2].ipv4+'\n'+'netmask '+host_info.ifaceInfo_list[2].netmask
		for line in f:
			if(line.startswith('iface lo')):
				lines=lines+[new_line]
			f.writelines(lines)
	os.system("scp "+current_path+"/interfaces/interfaces"+h_name+" root@"+host_info.ifaceInfo_list[2].ipv4+":/root/")

if __name__ == "__main__":
	if len(sys.argv) > 1:
		part_host_interfaces_clean(host_name=sys.argv[1])
	else:
		all_host_interfaces_clean()
