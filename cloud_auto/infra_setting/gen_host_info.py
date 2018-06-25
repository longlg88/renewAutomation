#!/usr/bin/python3

import os
import sys
import requests
import value_setting
import json

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from glogger import Logger
from collections import OrderedDict

sys.path.insert(0,'../')
import host

json_dto = OrderedDict()
json_pport_dto = OrderedDict()
logger=Logger()
def host_main(file_path, ssh, resource_mul, hostid):

	if os.path.isfile("../config/user_mng") == False and os.path.isfile("../config/user_pw_mng") == False:
		logger.error("execute user_account_mng program")
		sys.exit()
	else:
		f_user=open("../config/user_mng")
		f_user_pw=open("../config/user_pw_mng")
	host_info_list=host.InfoList(file_path)         # host_info_list define
	
	##value initial define
	dict_host = []
	gen_current_path=os.path.realpath(__file__)
	current_path=gen_current_path.split('/')[-1]
	logger.info("==============================================")
	logger.info("****  This log is for "+current_path.split('.')[0]+" host main ****")
	_insert_sql_host=open('../ansible/files/sql_script/insert/insert_host.sql','w')
	_insert_sql_hostresource=open('../ansible/files/sql_script/insert/insert_hostresource.sql','w')
	_insert_sql_pport=open('../ansible/files/sql_script/insert/insert_pport.sql','w')

	_file_for_sysmanageragent=open('../ansible/files/file_for_sysmanageragent','w')

	_host_id=1000000001 + int(hostid)
	_pport_id=1000000001 + (int(hostid) *3)
	for host_info in host_info_list.HostInfo_list:
		#h_name=host_info.host_name
		#h_tag=host_info.tag
		line_user=f_user.readline()
		line_user_pw=f_user_pw.readline()
		#print(" id = ",line_user.strip())
		#print(" pw = ",line_user_pw.strip())

		hostname=host_info.host_name
		if(file_path == "../config/host_info"):
			hostIP=host_info.ifaceInfo_list[4].ipv4
		elif(file_path == "../config/host_info_lite"):
			hostIP=host_info.ifaceInfo_list[4].ipv4
		ssh.connect(hostIP, look_for_keys=True)
		totalcpu=value_setting.cpu_info(ssh)
		totalmemory=value_setting.mem_info(ssh)
		totalsize=value_setting.disk_info(ssh)
		accessname=line_user.strip()
		accessauth=line_user_pw.strip()
		vtotalcpu=int(totalcpu)*int(resource_mul)
		vtotalmemory=int(totalmemory)*int(resource_mul)

		## iface_name is deprecated in 20180531
		## because, it is defficult to find mac address using network interface name
		#iface_name=[]
		#iface_name.append(host_info.ifaceInfo_list[0].iface_name)
		#iface_name.append(host_info.ifaceInfo_list[1].iface_name)
		#iface_name.append(host_info.ifaceInfo_list[2].iface_name)
		#iface_name.append(host_info.ifaceInfo_list[3].iface_name)
		#iface_name.append(host_info.ifaceInfo_list[4].iface_name)
		#print('iface_name = ',iface_name)
		iface_ip=[]
		if(host_info.tag == "Master"):
			iface_ip.append(host_info.ifaceInfo_list[1].ipv4)
		else:
			iface_ip.append(host_info.ifaceInfo_list[0].ipv4)

		iface_ip.append(host_info.ifaceInfo_list[3].ipv4)
		iface_ip.append(host_info.ifaceInfo_list[4].ipv4)
		mac_addr=value_setting.mac_info(iface_ip, ssh)
		
		if(host_info.tag == "Master"):
			nodetype=0
			h_type='Master'
			DIR_SQL='./sql/master/'
		elif(host_info.tag == "Compute"):
			nodetype=1
			h_type='Compute'
			DIR_SQL='./sql/compute/'
		elif(host_info.tag == "Storage"):
			nodetype=2
			h_type='Storage'
			DIR_SQL='./sql/storage/'
		elif(host_info.tag == "LB"):
			nodetype=1
			h_type='Compute'
		
		if(host_info.tag != "Storage"):
			file_sys=str(host_info.ifaceInfo_list[4].ipv4)+" "+str(_host_id)+"\n"
			_file_for_sysmanageragent.writelines(file_sys)
		
		sql_host="INSERT INTO HOSTINFO(HOSTID, HOSTNAME, HYPERVISORTYPE, CPUARCH, TOTALCPU, TOTALMEMORY, TOTALDISK, ACCESSNAME, ACCESSAUTH, CREATEDTIME, UPDATEDTIME, DESCRIPTION, ACCESSPORT) VALUES("+str(_host_id)+", '"+str(hostname)+"', "+"'LXC', 'x86_64', "+str(totalcpu)+", "+str(totalmemory)+", "+str(totalsize)+", '"+str(accessname)+"', '"+str(accessauth)+"', SYSTIMESTAMP, SYSTIMESTAMP, '',22);\n"

		sql_hostresource="INSERT INTO HOSTRESOURCEINFO(HOSTID, STATUS, ACTIVE, HOSTTYPE, NODETYPE, VTOTALCPU, VFREECPU, VTOTALMEMORY, VFREEMEMORY, POOLEDDISK, FREEDISK, CREATEDTIME, UPDATEDTIME, DESCRIPTION, AVAILABILITYZONE) VALUES("+str(_host_id)+", "+"'RUNNING', 1, '"+str(h_type)+"', "+str(nodetype)+", "+str(vtotalcpu)+", "+str(vtotalcpu)+", "+str(vtotalmemory)+", "+str(vtotalmemory)+", "+str(totalsize)+", "+str(totalsize)+", SYSTIMESTAMP, SYSTIMESTAMP, '','');\n"

		sql_pportinfo_1="INSERT INTO PPORTINFO(PPORTID, NAME, HOSTID, NETWORKTYPE, VLANID, IPADDR, MACADDR, PMACADDR, PORT, AGGREGATEDPORT, SWITCHDPID, SWITCHPORT, SWITCHNAME, ISACTIVE, ISAGGREGATED, DESCRIPTION, CREATEDTIME, UPDATEDTIME, SUBNETUUID, IPVALUE) VALUES("+str(_pport_id)+", '"+str('%08X'%(_pport_id))+"', "+str(_host_id)+", 'I', 0, '"+str(host_info.ifaceInfo_list[4].ipv4)+"', '"+str(mac_addr[2])+"', '"+str(mac_addr[2])+"', '"+str(host_info.ifaceInfo_list[0].vlan_raw_dev)+"','', '"+str(host_info.ifaceInfo_list[1].switch_dpid)+"', '"+str(host_info.ifaceInfo_list[1].switch_port)+"', 'Legacy-switch', 1, 0, '', SYSTIMESTAMP, SYSTIMESTAMP,'',0);\n"

		_pport_id = _pport_id+1
		sql_pportinfo_2="INSERT INTO PPORTINFO(PPORTID, NAME, HOSTID, NETWORKTYPE, VLANID, IPADDR, MACADDR, PMACADDR, PORT, AGGREGATEDPORT, SWITCHDPID, SWITCHPORT, SWITCHNAME, ISACTIVE, ISAGGREGATED, DESCRIPTION, CREATEDTIME, UPDATEDTIME, SUBNETUUID, IPVALUE) VALUES("+str(_pport_id)+", '"+str('%08X'%(_pport_id))+"', "+str(_host_id)+", 'M', 3, '"+str(host_info.ifaceInfo_list[3].ipv4)+"', '"+str(mac_addr[1])+"', '"+str(mac_addr[1])+"', '"+str(host_info.ifaceInfo_list[0].vlan_raw_dev)+"','', '"+str(host_info.ifaceInfo_list[1].switch_dpid)+"', '"+str(host_info.ifaceInfo_list[1].switch_port)+"', 'Legacy-switch', 1, 0, '', SYSTIMESTAMP, SYSTIMESTAMP,'',0);\n"

		_pport_id = _pport_id+1
		sql_pportinfo_3="INSERT INTO PPORTINFO(PPORTID, NAME, HOSTID, NETWORKTYPE, VLANID, IPADDR, MACADDR, PMACADDR, PORT, AGGREGATEDPORT, SWITCHDPID, SWITCHPORT, SWITCHNAME, ISACTIVE, ISAGGREGATED, DESCRIPTION, CREATEDTIME, UPDATEDTIME, SUBNETUUID, IPVALUE) VALUES("+str(_pport_id)+", '"+str('%08X'%(_pport_id))+"', "+str(_host_id)+", 'F', 2, '"+str(host_info.ifaceInfo_list[1].ipv4)+"', '"+str(mac_addr[0])+"', '"+str(mac_addr[0])+"', '"+str(host_info.ifaceInfo_list[0].vlan_raw_dev)+"','', '"+str(host_info.ifaceInfo_list[1].switch_dpid)+"', '"+str(host_info.ifaceInfo_list[1].switch_port)+"', 'Legacy-switch', 1, 0, '', SYSTIMESTAMP, SYSTIMESTAMP,'',0);\n"
		if(host_info.tag != "Master"):
			sql_pportinfo_3="INSERT INTO PPORTINFO(PPORTID, NAME, HOSTID, NETWORKTYPE, VLANID, IPADDR, MACADDR, PMACADDR, PORT, AGGREGATEDPORT, SWITCHDPID, SWITCHPORT, SWITCHNAME, ISACTIVE, ISAGGREGATED, DESCRIPTION, CREATEDTIME, UPDATEDTIME, SUBNETUUID, IPVALUE) VALUES("+str(_pport_id)+", '"+str('%08X'%(_pport_id))+"', "+str(_host_id)+", 'F', 2, '"+str(host_info.ifaceInfo_list[0].ipv4)+"', '"+str(mac_addr[0])+"', '"+str(mac_addr[0])+"', '"+str(host_info.ifaceInfo_list[0].vlan_raw_dev)+"','', '"+str(host_info.ifaceInfo_list[1].switch_dpid)+"', '"+str(host_info.ifaceInfo_list[1].switch_port)+"', 'Legacy-switch', 1, 0, '', SYSTIMESTAMP, SYSTIMESTAMP,'',0);\n"

		_host_id=_host_id+1
		_pport_id=_pport_id+1

		logger.info(sql_host)
		logger.info(sql_hostresource)
		logger.info(sql_pportinfo_1)
		logger.info(sql_pportinfo_2)
		logger.info(sql_pportinfo_3)
		#ssh.close()
		_insert_sql_host.writelines(sql_host)
		_insert_sql_hostresource.writelines(sql_hostresource)
		_insert_sql_pport.writelines(sql_pportinfo_1)

		_insert_sql_pport.writelines(sql_pportinfo_2)
		_insert_sql_pport.writelines(sql_pportinfo_3)

	_insert_sql_host.writelines("commit;\n")
	_insert_sql_host.writelines("exit")
	_insert_sql_host.close()
	
	_insert_sql_hostresource.writelines("commit;\n")
	_insert_sql_hostresource.writelines("exit")
	_insert_sql_hostresource.close()

	_insert_sql_pport.writelines("commit;\n")
	_insert_sql_pport.writelines("exit")
	_insert_sql_pport.close()

	_file_for_sysmanageragent.close()
	logger.info("==============================================")
	logger.info("\n")
	f_user.close()
	f_user_pw.close()

'''
		## pooledDisk is deciding ...
		json_host = {'hostName':hostname, 'hostType':host_info.tag, 'hypervisorType':'LXC', 'cpuArch':'x86_64', 'totalCpu': totalcpu, 'totalMemory': totalmemory, 'totalDisk':totalsize, 'pooledDisk': totalsize, 'freeDisk':totalsize, 'availabilityZone':'', 'status':'Start', 'accessName': accessname, 'accessAuth':accessauth, 'description':'', 'meta':'','active':True, 'nodeType':nodetype, 'vTotalCpu': vtotalcpu, 'vFreeCpu': vtotalcpu, 'vTotalMemory': vtotalmemory, 'vFreeMemory': vtotalmemory, 'accessPort': 22}
		dict_host.append(json_host)
		json_dto["dto"]=json_host
		DIR_PATH='./'
		if not os.path.exists(DIR_JSON):
			os.makedirs(DIR_JSON, exist_ok=True)
		with open(DIR_JSON+hostname+'.json', 'w', encoding='utf-8') as make_file:
			json.dump(json_dto, make_file, ensure_ascii=False, indent="\t", sort_keys=True)
	'''
## log...
#_data_name=str(hostname)+" name : "+hostname
#_data_totalcpu =str(hostname)+" cpu : "+str(totalcpu)
#_data_totalmemory =str(hostname)+ " memory : "+str(totalmemory)
#_data_totalsize =str(hostname)+ " disk : "+str(totalsize)
#_data_accessname =str(hostname)+ " user id : "+str(accessname)
#_data_accessauth =str(hostname)+ " user pw : "+str(accessauth)
##_data_vtotalcpu =str(hostname)+ " vCpu : "+str(vtotalcpu)
#_data_vtotalmemory =str(hostname)+ " vMemory : "+str(vtotalmemory)
#logger.info(_data_name)
#logger.info(_data_totalcpu)
#logger.info(_data_totalmemory)
#logger.info(_data_totalsize)
#logger.info(_data_accessname)
#logger.info(_data_accessauth)
#logger.info(_data_vtotalcpu)
#logger.info(_data_vtotalmemory)
#		else:
#			print('there is no EXIST, error')
#			sys.exit()
## file delete 

def pport_main(file_path, ssh):
	host_info_list=host.InfoList(file_path)

	dict_pport=[]
	gen_current_path=os.path.realpath(__file__)
	current_path=gen_current_path.split('/')[-1]
	logger.info("==============================================")
	logger.info("**** This log is for "+current_path.split('.')[0]+" pport main ****")

	## host service outdto json parsing
	f=open("../ansible/vars/common_vars.yml",'r')
	lines=f.readlines()
	master_ip="".join([s.split(":")[-1] for s in lines if 'master_ip' in s][0]).replace('\n','')
	master_ip=master_ip.replace(' ','')
	if(master_ip == ""):
		logger.error("There is no master_ip, setting ../ansible/vars/common_vars.yml")
		sys.exit()
	res = requests.get("http://"+master_ip+":8080/imp/master/Hosts?action=List")
	DIR_JSON='./json/get/'
	if not os.path.exists(DIR_JSON):
		os.makedirs(DIR_JSON, exist_ok=True)
	with open(DIR_JSON+'host.json','w',encoding='utf-8') as make_file:
		json.dump(res.json(), make_file, ensure_ascii=False, indent='\t', sort_keys=True)
		logger.info("Generate host service json...")
	with open(DIR_JSON+'host.json') as data_file:
		data=json.load(data_file)

	print("totalNum= ",data['dto']['totalNum'])
	host_total=int(data['dto']['totalNum'])

#	json_pport_all=[]
	## pport service indto json generate
	for num in range(0, host_total):
		for host_info in host_info_list.HostInfo_list:
			iface_name=[]
			if(file_path == "../config/host_info_lite"):
				iface_name.append(host_info.ifaceInfo_list[1].iface_name)
			else:
				iface_name.append(host_info.ifaceInfo_list[0].iface_name)
				iface_name.append(host_info.ifaceInfo_list[1].iface_name)
				iface_name.append(host_info.ifaceInfo_list[2].iface_name)
			## return mac_addr = ["Frontend","Management","Internal"]
			
			if(data['dto']['hosts'][num]['hostName'] == host_info.host_name):
				if(file_path == "../config/host_info_lite"):
					hostIP=host_info.ifaceInfo_list[1].ipv4
				else:
					hostIP=host_info.ifaceInfo_list[2].ipv4

				ssh.connect(hostIP, look_for_keys=True)
				mac_addr=value_setting.mac_info(iface_name, ssh)
				#logger.info('mac addr = '+mac_addr)
				host_id=int("0x"+data['dto']['hosts'][num]['hostUuid'],16)

				if(file_path == "../config/host_info_lite"):
					json_pport_1={'name':'pport_'+data['dto']['hosts'][num]['hostName'], 'hostId':host_id, 'networkType':'F', 'ipAddr':host_info.ifaceInfo_list[1].ipv4, 'macAddr':mac_addr[4], 'pmacAddr':'', 'port':host_info.ifaceInfo_list[0].iface_name, 'aggregatedPort':'', 'switchDpid':0, 'switchPort':0, 'switchName':'Legacy switch', 'isActive':1, 'isAggregated':0, 'description':'','vlanId':0}

				## json for pport / needs 3 json(Frontend, Management, Internal)
				else:
					json_pport_1={'name':'pport_'+data['dto']['hosts'][num]['hostName'], 'hostId':host_id, 'networkType':'I', 'ipAddr':host_info.ifaceInfo_list[2].ipv4, 'macAddr':mac_addr[2], 'pmacAddr':'', 'port':host_info.ifaceInfo_list[2].iface_name, 'aggregatedPort':'', 'switchDpid':host_info.ifaceInfo_list[0].switch_dpid, 'switchPort':host_info.ifaceInfo_list[0].switch_port, 'switchName':'Edge-Core','isActive':1, 'isAggregated':0, 'description':'','vlanId':0}
					json_pport_2={'name':'pport_'+data['dto']['hosts'][num]['hostName'], 'hostId':host_id, 'networkType':'M', 'ipAddr':host_info.ifaceInfo_list[1].ipv4, 'macAddr':mac_addr[1], 'pmacAddr':host_info.ifaceInfo_list[1].pseudomac, 'port':host_info.ifaceInfo_list[1].vlan_raw_dev, 'aggregatedPort':'', 'switchDpid':host_info.ifaceInfo_list[0].switch_dpid, 'switchPort':host_info.ifaceInfo_list[0].switch_port, 'switchName':'Edge-Core', 'isActive':1, 'isAggregated':0, 'description':'', 'vlanId':3}
					json_pport_3={'name':'pport_'+data['dto']['hosts'][num]['hostName'], 'hostId':host_id, 'networkType':'F', 'ipAddr':host_info.ifaceInfo_list[0].ipv4, 'macAddr':mac_addr[0], 'pmacAddr':host_info.ifaceInfo_list[0].pseudomac, 'port':host_info.ifaceInfo_list[0].vlan_raw_dev, 'aggregatedPort':'', 'switchDpid':host_info.ifaceInfo_list[0].switch_dpid, 'switchPort':host_info.ifaceInfo_list[0].switch_port, 'switchName':'Edge-Core', 'isActive':1, 'isAggregated':0, 'description':'','vlanId':2}
			
				DIR_JSON='./json/pport/'
				if not os.path.exists(DIR_JSON):
					os.makedirs(DIR_JSON, exist_ok=True)
				if(file_path == "../config/host_info_lite"):
					with open(DIR_JSON+host_info.host_name+'.json','w',encoding='utf-8') as make_file:
						json_pport_dto['dto']=json_pport_1
						json.dump(json_pport_dto, make_file, ensure_ascii=False, indent='\t', sort_keys=True)
				else:

					with open(DIR_JSON+host_info.host_name+'_1.json','w',encoding='utf-8') as make_file:
	#					dict_pport.append(json_pport)
						json_pport_dto['dto']=json_pport_1
						json.dump(json_pport_dto, make_file, ensure_ascii=False, indent='\t', sort_keys=True)
					with open(DIR_JSON+host_info.host_name+'_2.json','w',encoding='utf-8') as make_file:
						json_pport_dto['dto']=json_pport_2
						json.dump(json_pport_dto, make_file, ensure_ascii=False, indent='\t', sort_keys=True)
					with open(DIR_JSON+host_info.host_name+'_3.json','w',encoding='utf-8') as make_file:
						json_pport_dto['dto']=json_pport_3
						json.dump(json_pport_dto, make_file, ensure_ascii=False, indent='\t', sort_keys=True)
					
				ssh.close()

#		host_uuid.append(int("0x"+data['dto']['hosts'][num]['hostUuid'], 16))
#		host_type.append(data['dto']['hosts'][num]['hostType'])
#	print(host_uuid)
