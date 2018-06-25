#!/usr/bin/python

import json
import os
from pprint import pprint

if __name__=="__main__":
	current_path=os.path.dirname(os.path.abspath(__file__))
	data=json.load(open(current_path+"/get_image.json"))
	with open(current_path+'/get_uuid','w') as get_uuid_file:
		for image  in data['dto']['listResult']:
			get_uuid_file.write(image['imageName']+":"+image['imageUuid']+"\n")
