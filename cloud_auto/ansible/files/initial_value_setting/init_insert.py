#!/usr/bin/python3
import os, sys, requests, json
from pprint import pprint
#import init_make_json

sys.path.append('/root/cloud_auto/')
import host
import utils

if __name__ == "__main__":
	### host info insert
	f=open("../vars/external_vars.yml",'r')
	lines=f.readlines()
	url_ip = "".join([s.split(":")[-1] for s in lines if 'master_ip' in s][0]).replace('\n','').replace(' ','')
	print(url_ip)
	tenantuuid = input("tenant uuid = ")
	## iaas
#	res_iaas = requests.post("http://"+url_ip+":8080/imp/master/Hosts", data=json.dumps("./json/Master/Master_iaas.json"))
#	print("res_iaas status code =  " + res_iaas.status_code + ", text = " + res_iaas.text)
	
	## tcnm
#	res_tcnm = requests.post("http://"+url_ip+":8080/imp/master/Hosts", data=json.dumps("./json/Master/Master_tcnm.json"))
#	print("res_tcnm status code = "+res_tcnm.status_code + ", text = " + res_tcnm.text)
	
	## portal
#	res_portal = requests.post("http://"+url_ip+":8080/imp/master/Hosts", data=json.dumps("./json/Master/Master_portal.json"))
#	print("res_portal status code = "+res_portal.status_code+", text = "+res_portal.text)

	## sysmanager
#	res_sysmanager = requests.post("http://"+url_ip+":8080/imp/master/Hosts", data=json.dumps("./json/Master/Master_sysmanager.json"))
#	print("res_sysmanager status code = "+res_sysmanager.status_code+", text = "+res_sysmanager.text)

	## backend network
#	res_back_net = requests.post("http://"+url_ip+":8080/imp/master/networks?tenantUuid="+tenantuuid, data=json.dumps("./json/network/net_backend.json"))
#	print("res_back_net status code = "+res_net.status_code+", text = "+res_net.text)

	## frontend network
#	res_front_net = requests.post("http://"+url_ip+":8080/imp/master/networks?tenantUuid="+tenantuuid, data=json.dumps("./json/network/net_frontend.json"))
#	print("res_front_net status code = "+res_front_net.status_code+", text = "+res_front_net.text)

	## management network
#	res_management_net = requests.post("http://"+url_ip+":8080/imp/master/networks?tenantUuid="+tenantuuid, data=json.dumps("./json/network/net_management.json"))
#	print("res_management_net status code = "+res_management_net.status_code+", text = "+res_management_net.text)

	## frontend network uuid get
	res_f_net_get = requests.get("http://"+url_ip+":8080/imp/master/networks?action=List&tenantUuid="+tenantuuid+"&sort=createdTime&offset=1&limit=1&type=1")
	DIR_JSON='./json/get'
	if not os.path.exists(DIR_JSON):
		os.makedirs(DIR_JSON, exist_ok=True)
	with open(DIR_JSON+"/backend_net_get.json", 'w', encoding="utf-8") as make_file:
		json.dump(res_f_net_get.json(), make_file, ensure_ascii=False, indent="\t", sort_keys=True)
	with open(DIR_JSON+"/backend_net_get.json") as data_file:
		data = json.load(data_file)

	pprint(data)
	net_uuid = data['dto']['networks'][0]['networkUuid']
	print("net uuid = "+net_uuid.lower())




	## subnet
#	res_subnet = requests.post("http://"+url_ip+":8080/imp/master/subnets?networkUuid="+net_uuid.lower(), data=json.dumps("./json/subnet.json"))
#	print("res_subnet status code = " + res_subent.status_code+", text="+res_subnet.text)
