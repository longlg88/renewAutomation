import os

with open("./roles/iaas_run/files/IaaSconfig","r") as f:
	data = f.readlines()

with open("./string_copy.tmp","w") as f:
	for line in data:
		line = line.strip()
		strlist = line.split('=')
		print( strlist )
		if strlist[0] == '': continue
#		f.write("    - { exp: \'" + strlist[1] + "\', rep: \'{{ " + strlist[0] + " }}\' }\n" )
		f.write("    " + strlist[0] + ": \"{{ " + strlist[1].strip('@') + " }}\"\n")
