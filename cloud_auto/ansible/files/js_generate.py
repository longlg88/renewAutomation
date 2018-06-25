import os, sys
import re
from glob import glob
import time

if len(sys.argv) != 4:
	print("usage : replacer [txt_src] [txt_dst] [dir]")
	sys.exit()
args = []
for arg in sys.argv : args.append(arg)

replace_src = args[1]
replace_dst = args[2]

target_path = args[3]

#target_path = input("Input target path (search js file) : ")

js_list  = [ file_path for dp, dn, filenames in os.walk(target_path) for file_path in glob(os.path.join(dp,'*.js'))]

#replace_src = input("Input replace target : ")
#replace_dst = input("Input replace destination : ")

home=os.getcwd()
print(home)
if os.access(home+'/rlog', os.F_OK) != True:
    os.mkdir(home+'/rlog')

with open(home+"/rlog/rlog_"+replace_src+"_"+replace_dst+"_"+time.strftime("%H-%M-%S"),'w') as log_fd:
	for target_file in js_list:
		print(target_file)
		target_src_list = []
		with open(target_file,'r') as f:
			data = f.readlines()
		lnum = -1
		for line in data:
			lnum += 1
			idx = 0
			while idx < len(line):
				idx = line.find(replace_src, idx)
				if idx == -1:
					break
				target_src_list.append(str(lnum)+", "+str(idx))
				idx = idx+len(replace_src)
		
		if len(target_src_list) == 0:
			continue
		else:	
			log_fd.write("*" + target_file + "\n")
			log_fd.write("The number of replaced src : "+str(len(target_src_list))+"\n")
			for stri in target_src_list:
				log_fd.write(stri+"\n")
			log_fd.write("\n")	
for target_file in js_list:
	with open(target_file, 'r') as f:
		data = f.read()
	data = data.replace(replace_src,replace_dst)
	with open(target_file, 'w') as f:
		f.write(data)
