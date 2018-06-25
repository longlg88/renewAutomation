#!/usr/bin/python3

import os
import sys
import math

## extract remote host cpu info
def cpu_info(ssh):
    stdin, stdout, stderr = ssh.exec_command("sudo -S grep -c processor /proc/cpuinfo")
    cpu_parsing = stdout.readlines()
    cpu_data=''.join(data.replace('\n', '') for data in cpu_parsing)
    return int(cpu_data)

## extract remote host memory info
def mem_info(ssh):
    stdin, stdout, stderr = ssh.exec_command("sudo -S cat /proc/meminfo | grep MemFree")
    mem_parsing = stdout.readlines()
    mem_data = ''.join(data.replace('\n','') for data in mem_parsing)
    mem_data = mem_data.replace('MemFree', '')
    mem_data = mem_data.replace(':','')
    mem_data = mem_data.replace('kB','')
    mem_data = mem_data.replace(' ','')
    mem_data = math.floor(int(mem_data) / 1000)
    return int(mem_data)

## extract remote host disk info
def disk_info(ssh):
    stdin, stdout, stderr = ssh.exec_command("sudo -S df -P | grep -v ^Filesystem | grep -v ^none | grep -v ^zvolume | awk '{sum += $2 } END {print sum/1024/1024; }'")
    disk_parsing = stdout.readlines()
    disk_data = ''.join(data.replace('\n', '') for data in disk_parsing)
    disk_data = math.floor(float(disk_data))
    return int(disk_data)

def mac_info(iface_ip, ssh):
	print(iface_ip)
	mac=[]
	for i in range(0, len(iface_ip)):
#		ip a | grep 172.19.0.3 | awk 'NF>1{print $NF}'
#		command="sudo -S cat /sys/class/net/"+iface_name[i]+"/address"
		command="sudo -S ip a | grep "+iface_ip[i]+" | awk 'NF>1{print $NF}'"
		stdin, stdout, stderr = ssh.exec_command(command)
		iface_name_parsing=stdout.readlines()
		iface_name="".join(iface_name_parsing).replace('\n','')
		command_mac="sudo -S cat /sys/class/net/"+iface_name+"/address"
		stdin, stdout, stderr = ssh.exec_command(command_mac)
		mac_parsing = stdout.readlines()
		## mac_parsing = ['eno1.2    Link encap:Ethernet  HWaddr fe:b0:c1:07:00:00  \n']
		#mac_list="".join(mac_parsing).split(' ')
		#print("mac_list origin : ",mac_list)
		#print("mac_list = ",mac_list[-3])
		print("mac is = ",mac_parsing)
		mac_parsing="".join(mac_parsing).replace('\n','')
		mac.append(mac_parsing)
	print("all mac are = ",mac)	
	return mac
