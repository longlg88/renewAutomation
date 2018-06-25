#!/usr/bin/python3

import os
import sys
import requests
import json

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from glogger import Logger
from collections import OrderedDict
from pprint import pprint

json_dto=OrderedDict()
logger=Logger()

def network_main():
	_vars_file=open("../ansible/vars/common_vars.yml",'r')
	lines=_vars_file.readlines()
## _user_tenant_uuid / _user_tenant_id is deprecated

#	_user_tenant_uuid="".join([s.split(":")[-1] for s in lines if 'user_tenant_uuid' in s][0]).replace('\n','')
	_admin_tenant_uuid="".join([s.split(":")[-1] for s in lines if 'admin_tenant_uuid' in s][0]).replace('\n','')

#	_user_tenant_id=int(_user_tenant_uuid, 16)
	_admin_tenant_id=int(_admin_tenant_uuid, 16)

	_insert_network_file=open('../ansible/files/sql_script/insert/insert_network.sql','w')
	net_info="INSERT INTO NetworkInfo(networkId, vlanId, tenantId, networkUuid, name, type, createdTime, status) VALUES(100000006, 6, "+str(_admin_tenant_id)+", '05F5E106', 'Front-End', 1, SYSTIMESTAMP, 'Active'); \nINSERT INTO NetworkInfo(networkId, vlanId, tenantId, networkUuid, name, type, createdTime, status) VALUES(100000005, 5, "+str(_admin_tenant_id)+", '05F5E105', 'Host-front', 3, SYSTIMESTAMP, 'Active'); \nINSERT INTO NetworkInfo(networkId, vlanId, tenantId, networkUuid, name, type, createdTime, status) VALUES(100000007, 7, "+str(_admin_tenant_id)+", '05F5E107', 'Management', 2, SYSTIMESTAMP, 'Active');\n commit; \n exit; \n"
	logger.info(net_info)
	_insert_network_file.writelines(net_info)
	_insert_network_file.close()
	_vars_file.close()

	'''
	# it's working for network service to add network database
	print(" enter network name")
	_input=input()
	dict_network={'name':_input, 'type':1}
	json_dto["dto"]=dict_network
	DIR_JSON='./json/network'
	if not os.path.exists(DIR_JSON):
		os.makedirs(DIR_JSON, exist_ok=True)
	with open(DIR_JSON+'/'+'network_front.json','w',encoding='utf-8') as make_file:
		json.dump(json_dto, make_file, ensure_ascii=False, indent='\t', sort_keys=True)
	'''

def subnet_main():
	_vars_file=open("./infra_info",'r')
	lines=_vars_file.readlines()

	h_ipaddr="".join([s.split(":")[-1] for s in lines if 'h_ipaddr' in s][0]).replace('\n','')
	h_netmask="".join([s.split(":")[-1] for s in lines if 'h_netmask' in s][0]).replace('\n','')
	h_cidr="".join([s.split(":")[-1] for s in lines if 'h_cidr' in s][0]).replace('\n','')
	h_gateway="".join([s.split(":")[-1] for s in lines if 'h_gateway' in s][0]).replace('\n','')
	h_dns="".join([s.split(":")[-1] for s in lines if 'h_dns' in s][0]).replace('\n','')

	f_ipaddr="".join([s.split(":")[-1] for s in lines if 'f_ipaddr' in s][0]).replace('\n','')
	f_netmask="".join([s.split(":")[-1] for s in lines if 'f_netmask' in s][0]).replace('\n','')
	f_cidr="".join([s.split(":")[-1] for s in lines if 'f_cidr' in s][0]).replace('\n','')
	f_gateway="".join([s.split(":")[-1] for s in lines if 'f_gateway' in s][0]).replace('\n','')
	f_dns="".join([s.split(":")[-1] for s in lines if 'f_dns' in s][0]).replace('\n','')
	
	v_ipaddr="".join([s.split(":")[-1] for s in lines if 'v_ipaddr' in s][0]).replace('\n','')
	v_netmask="".join([s.split(":")[-1] for s in lines if 'v_netmask' in s][0]).replace('\n','')
	v_cidr="".join([s.split(":")[-1] for s in lines if 'v_cidr' in s][0]).replace('\n','')
	v_gateway="".join([s.split(":")[-1] for s in lines if 'v_gateway' in s][0]).replace('\n','')
	v_dns="".join([s.split(":")[-1] for s in lines if 'v_dns' in s][0]).replace('\n','')

	m_ipaddr="".join([s.split(":")[-1] for s in lines if 'm_ipaddr' in s][0]).replace('\n','')
	m_netmask="".join([s.split(":")[-1] for s in lines if 'm_netmask' in s][0]).replace('\n','')
	m_cidr="".join([s.split(":")[-1] for s in lines if 'm_cidr' in s][0]).replace('\n','')
	m_gateway="".join([s.split(":")[-1] for s in lines if 'm_gateway' in s][0]).replace('\n','')
	m_dns="".join([s.split(":")[-1] for s in lines if 'm_dns' in s][0]).replace('\n','')

	b_ipaddr="".join([s.split(":")[-1] for s in lines if 'b_ipaddr' in s][0]).replace('\n','')
	b_netmask="".join([s.split(":")[-1] for s in lines if 'b_netmask' in s][0]).replace('\n','')
	b_cidr="".join([s.split(":")[-1] for s in lines if 'b_cidr' in s][0]).replace('\n','')
	b_gateway="".join([s.split(":")[-1] for s in lines if 'b_gateway' in s][0]).replace('\n','')
	b_dns = "".join([s.split(":")[-1] for s in lines if 'b_dns' in s][0]).replace('\n','')

	_insert_subnet_file=open('../ansible/files/sql_script/insert/insert_subnet.sql','w')

	subnet_info="INSERT INTO SUBNETINFO (subnetId, networkId, subnetUuid, ipAddr, netmask, cidr, gateway, dns, vlanId, name, type, isLb, createdTime, isHost, status) VALUES (100000000, 100000005, '05F5E100', '"+h_ipaddr.replace(' ','')+"', '"+h_netmask.replace(' ','')+"', "+h_cidr.replace(' ','')+", '"+h_gateway.replace(' ','')+"', '"+h_dns.replace(' ','')+"', 5, 'Host-Subnet', 3, 0, SYSTIMESTAMP, 1, 'Active');" + \
"\nINSERT INTO SUBNETINFO (subnetId, networkId, subnetUuid, ipAddr, netmask, cidr, gateway, dns, vlanId, name, type, isLb, createdTime, isHost, status) VALUES (100000001, 100000006, '05F5E101', '"+f_ipaddr.replace(' ','')+"', '"+f_netmask.replace(' ','')+"', "+f_cidr.replace(' ','')+", '"+f_gateway.replace(' ','')+"', '"+f_dns.replace(' ','')+"', 6, 'Front-Subnet', 1, 0, SYSTIMESTAMP, 0, 'Active');" + \
"\nINSERT INTO SUBNETINFO (subnetId, networkId, subnetUuid, ipAddr, netmask, cidr, gateway, dns, vlanId, name, type, isLb, createdTime, isHost, status) VALUES (100000002, 100000006, '05F5E102', '"+v_ipaddr.replace(' ','')+"', '"+v_netmask.replace(' ','')+"', "+v_cidr.replace(' ','')+", '"+v_gateway.replace(' ','')+"', '"+v_dns.replace(' ','')+"', 6, 'Vip-Subnet', 1, 1, SYSTIMESTAMP, 0, 'Active');" + \
"\nINSERT INTO SUBNETINFO (subnetId, networkId, subnetUuid, ipAddr, netmask, cidr, gateway, dns, vlanId, name, type, isLb, createdTime, isHost, status) VALUES (100000003, 100000007, '05F5E103', '"+m_ipaddr.replace(' ','')+"', '"+m_netmask.replace(' ','')+"', "+m_cidr.replace(' ','')+", '"+m_gateway.replace(' ','')+"', '"+m_dns.replace(' ','')+"', 7, 'Management-Subnet', 2, 0, SYSTIMESTAMP, 0, 'Active');" + \
"\ncommit;\nexit; \n"

	logger.info(subnet_info)
	_insert_subnet_file.writelines(subnet_info)
	_insert_subnet_file.close()
	_vars_file.close()
	
	'''
	# it's working for subnet service to add subnet database
	_sn_name=input(" enter subnet name")
	_sn_ipAddr=input(" enter subnet ip addr")
	_sn_netmask=input(" enter subnet netmask")
	_sn_gateway=input(" enter subnet gateway")
	_sn_dns=input(" enter dns")
	_sn_isLb=input(" enter is LB 0/1")
	dict_subnet = {'name':_sn_name, 'ipAddr':_sn_ipAddr, 'netmask':_sn_netmask, 'gateway':_sn_gateway, 'dns':_sn_dns, 'isLb':_sn_isLb }
	json_dto["dto"]=dict_subnet
	DIR_JSON='./json/subnet'
	if not os.path.exists(DIR_JSON):
		os.makedirs(DIR_JSON, exist_ok=True)
	with open(DIR_JSON+'/'+'subnet_'+_sn_name+'.json','w',encoding='utf-8') as make_file:
		json.dump(json_dto, make_file, ensure_ascii=False, indent='\t', sort_keys=True)
	'''

def getIpValue(ipAddr):
    cutIpAddr=ipAddr.split('.')
    hexIpAddr=[]
    for i in cutIpAddr:
        hexIpAddr.append(format(int(i), '#04x')[2:].lower())
    hexIpValue=""
    for j in hexIpAddr:
        if len(j) == 1:
            hexIpValue+="0"+j
        elif len(j) == 2:
            hexIpValue+=j
    return format(int(hexIpValue, 16))

#def vport_main(_vport_count):
def vport_main():
## deprecated ipvalue
#	pre="INSERT INTO VportInfo(vportId, mac1, mac2, ipAddr, macAddr, networkId, vlanId, ipvalue, subnetId, vportUuid, name, status, networkType, instanceId, targetPoolId, createdTime)"
	pre="INSERT INTO VportInfo(vportId, mac1, mac2, ipAddr, macAddr, networkId, vlanId, subnetId, vportUuid, name, status, networkType, instanceId, targetPoolId, createdTime)"
	pre_public="INSERT INTO PUBLICIPINFO(publicIp, publicIpId, publicIpUuid, vportId, createdTime)"

	vportId = 100000001
	publicId = 100000001
	networkId = 100000006
	subnetId = 100000001
	lb_subnetId = 100000002
	_vars_file=open("./infra_info",'r')
	_common_vars_file=open('../ansible/vars/common_vars.yml','r')
	lines=_vars_file.readlines()
	common_lines=_common_vars_file.readlines()

	_isSDN="".join([s.split(":")[-1] for s in common_lines if 'TCN_SDN_RUN' in s][0]).replace('\n','').replace(' ','')

#	if _isSDN == "ON":
#		_f_vport_args="".join([s.split(":")[-1] for s in lines if 'f_vports' in s][0]).replace('\n','').replace(' ','')

	_fp_vport_args="".join([s.split(":")[-1] for s in lines if 'fp_vports' in s][0]).replace('\n','').replace(' ','')
	
	_lb_vport_args="".join([s.split(":")[-1] for s in lines if 'lb_vports' in s][0]).replace('\n','').replace(' ','')
	
	_fp_vports_count="".join([s.split(":")[-1] for s in lines if 'fp_vports_count' in s][0]).replace('\n','').replace(' ','')
	_lb_vports_count="".join([s.split(":")[-1] for s in lines if 'lb_vports_count' in s][0]).replace('\n','').replace(' ','')

	_fp_vports_routine="".join([s.split(":")[-1] for s in lines if 'fp_vports_routine' in s][0]).replace('\n','').replace(' ','')
	_lb_vports_routine="".join([s.split(":")[-1] for s in lines if 'lb_vports_routine' in s][0]).replace('\n','').replace(' ','')

	_public_args="".join([s.split(":")[-1] for s in lines if 'public' in s][0]).replace('\n','').replace(' ','')
	_lb_public_args="".join([s.split(":")[-1] for s in lines if 'lb_public' in s][0]).replace('\n','').replace(' ','')

	
	#_f_vport_list=_f_vport_args.split(',')
	#_fp_vport_list=_fp_vport_args.split(',')
	#_lb_vport_list=_lb_vport_args.split(',')

	###########################################
	### _f_vport_list must make count logic ###
	###########################################

	### _fp_vport_list count logic ###
	_fp_vport_ipvalue_list=_fp_vport_args.split(".")
	_fp_vport_last_value=int(_fp_vport_ipvalue_list[3])
	_fp_vport_third_value=int(_fp_vport_ipvalue_list[2])
	_fp_vport_list=[]
	
	for j in range(int(_fp_vports_routine)):
		for i in range(int(_fp_vports_count)):
			_fp_vport_last_value=_fp_vport_last_value+1
			_fp_vport_list.append(_fp_vport_ipvalue_list[0]+'.'+_fp_vport_ipvalue_list[1]+'.'+str(_fp_vport_third_value)+'.'+str(_fp_vport_last_value-1))
			if _fp_vport_last_value == 256:
				_fp_vport_third_value=_fp_vport_third_value+1
				_fp_vport_last_value=2
	
	### _lb_vport_list count logic ###
	_lb_vport_ipvalue_list=_lb_vport_args.split('.')
	_lb_vport_last_value=int(_lb_vport_ipvalue_list[3])
	_lb_vport_third_value=int(_lb_vport_ipvalue_list[2])
	_lb_vport_list=[]
	for k in range(int(_lb_vports_routine)):
		for l in range(int(_lb_vports_count)):
			_lb_vport_last_value=_lb_vport_last_value+1
			_lb_vport_list.append(_lb_vport_ipvalue_list[0]+'.'+_lb_vport_ipvalue_list[1]+'.'+str(_lb_vport_third_value)+'.'+str(_lb_vport_last_value-1))
			if _lb_vport_last_value == 256:
				_lb_vport_third_value=_lb_vport_third_value+1
				_lb_vport_last_value=2


	_public_list=_public_args.split(',')
	_lb_public_list=_lb_public_args.split(',')

	_insert_vport_file=open('../ansible/files/sql_script/insert/insert_vport.sql','w')
	_insert_lb_vport_file=open('../ansible/files/sql_script/insert/insert_lb_vport.sql','w')
	_insert_public_file=open('../ansible/files/sql_script/insert/insert_public.sql','w')
	_insert_lb_public_file=open('../ansible/files/sql_script/insert/insert_lb_public.sql','w')

#	if _isSDN == "ON":
#		for _f_vports in _f_vport_list:
#			ipvalue=getIpValue(_f_vports)
#			vportUuid = format(int(vportId), '#04x')[2:].upper()
#			post=" VALUES("+str(vportId) +", "+"'0"+vportUuid+"'"+", 0, "+"'"+_f_vports+"'"+", 'none', "+str(networkId) + ", "+str(ipvalue)+", 2, "+str(subnetId)+", "+"'0"+vportUuid+"'"+", 'none', 'Active', 'F', NULL, NULL, SYSTIMESTAMP);\n"
#			vportId = vportId+1
#			vport_result=pre+post
#
#			logger.info(vport_result)
#			_insert_vport_file.writelines(vport_result)
	for _fp_vports in _fp_vport_list:
## deprecated ipvalue
#		ipvalue=getIpValue(_fp_vports)
		vportUuid = format(int(vportId), '#04x')[2:].upper()
#		post=" VALUES("+str(vportId) +", "+"'0"+vportUuid+"'"+", 0, "+"'"+_fp_vports+"'"+", 'none', "+str(networkId) + ", "+str(ipvalue)+", 5, "+str(subnetId)+", "+"'0"+vportUuid+"'"+", 'none', 'Active', 'FP', NULL, NULL, SYSTIMESTAMP);\n"
		post=" VALUES("+str(vportId) +", "+"'0"+vportUuid+"'"+", 0, "+"'"+_fp_vports+"'"+", 'none', "+str(networkId) + ", 6, "+str(subnetId)+", "+"'0"+vportUuid+"'"+", 'none', 'Active', 'FP', NULL, NULL, SYSTIMESTAMP);\n"
		vportId = vportId+1
		vport_result=pre+post

		logger.info(vport_result)
		_insert_vport_file.writelines(vport_result)

	_insert_vport_file.writelines("commit;\n")
	_insert_vport_file.writelines("exit;")
	_insert_vport_file.close()

	for _lb_vports in _lb_vport_list:
## deprecated ipvalue
#		ipvalue=getIpValue(_lb_vports)
		vportUuid = format(int(vportId), '#04x')[2:].upper()
#		post=" VALUES("+str(vportId) +", "+"'0"+vportUuid+"'"+", 0, "+"'"+_lb_vports+"'"+", 'none', "+str(networkId) +","+str(ipvalue)+", 5, "+str(lb_subnetId)+", "+"'0"+vportUuid+"'"+", 'none', 'Active', 'FLB', NULL, NULL, SYSTIMESTAMP);\n"
		post=" VALUES("+str(vportId) +", "+"'0"+vportUuid+"'"+", 0, "+"'"+_lb_vports+"'"+", 'none', "+str(networkId) +", 6, "+str(lb_subnetId)+", "+"'0"+vportUuid+"'"+", 'none', 'Active', 'FLB', NULL, NULL, SYSTIMESTAMP);\n"
		vportId=vportId+1
		lb_vport_result=pre+post
		logger.info(lb_vport_result)
		_insert_lb_vport_file.writelines(lb_vport_result)
	_insert_lb_vport_file.writelines("commit;\n")
	_insert_lb_vport_file.writelines("exit;")
	_insert_lb_vport_file.close()

	for _publics in _public_list:
		publicUuid=format(int(publicId), '#04x')[2:].upper()
		post_public=" VALUES('"+_publics+"', "+str(publicId)+", '0"+publicUuid+"', "+str(publicId)+", SYSTIMESTAMP);\n"
		publicId = publicId+1
		public_result=pre_public+post_public

		logger.info(public_result)
		_insert_public_file.writelines(public_result)

	_insert_public_file.writelines("commit;\n")
	_insert_public_file.writelines("exit;")
	_insert_public_file.close()

	for _lb_publics in _lb_public_list:
		publicUuid=format(int(publicId), '#04x')[2:].upper()
		post_public=" VALUES('"+_lb_publics+"', "+str(publicId)+", '0"+publicUuid+"', "+str(publicId)+", SYSTIMESTAMP);\n"
		publicId=publicId+1
		lb_public_result = pre_public+post_public
		logger.info(lb_public_result)
		_insert_lb_public_file.writelines(lb_public_result)

	_insert_lb_public_file.writelines("commit;\n")
	_insert_lb_public_file.writelines("exit;")
	_insert_lb_public_file.close()
	_vars_file.close()




	'''
def vport_main(_vport_count):
	## GET network service (network_uuid) / GET subnet service (subnet_uuid) / POST vport service as you want

	f=open('../ansible/vars/common_vars.yml','r')
	lines=f.readlines()
	im_ip = "".join([s.split(":")[-1] for s in lines if 'master_ip' in s][0]).replace('\n','').replace(' ','')
	_tenant_uuid = "".join([s.split(":")[-1] for s in lines if 'tenant_uuid' in s][0]).replace('\n','').replace(' ','')
	
	## GET network service (network_uuid)
	_net_res = requests.get("http://"+im_ip+":8080/imp/master/networks?action=List&tenantUuid="+_tenant_uuid+"&sort=createdTime&offset=1&limit=1&type=1")
	DIR_JSON='./json/get'
	if not os.path.exists(DIR_JSON):
		os.makedirs(DIR_JSON, exist_ok=True)
	with open(DIR_JSON+"/net_res.json",'w', encoding='utf-8') as make_file:
		json.dump(_net_res.json(), make_file, ensure_ascii=False, indent='\t', sort_keys=True)
	with open(DIR_JSON+"/net_res.json") as data_file:
		data=json.load(data_file)
	
	_net_uuid=data['dto']['networks'][0]['networkUuid']
	
	## GET subnet service (subnet_uuid)
	_subnet_res = requests.get("http://"+im_ip+":8080/imp/master/subnets?action=List&networkUuid="+_net_uuid.lower()+"&sort=createdTime&offset=1&limit=100&type=1")
	with open(DIR_JSON+'/subnet_res.json','w',encoding='utf-8') as make_file:
		json.dump(_subnet_res.json(), make_file, ensure_ascii=False, indent='\t', sort_keys=True)
	with open(DIR_JSON+'/subnet_res.json') as sn_data_file:
		data=json.load(sn_data_file)
	_subnet_uuid=data['dto']['subnets'][0]['subnetUuid']
	
	for i in range(0, _vport_count):
		_vport_req=requests.post("http://"+im_ip+":8080/imp/master/vports/subnetUuid="+_subnet_uuid)
		logger.info(i+". " + "_vport_req status code = "+_vport_req.status_code + ", text = " + _vport_req.text)
	## vports 다 만들고 public IP넣을껀지 or vports 만든다음 바로 public IP떄려 넣을건지
	
	'''	
