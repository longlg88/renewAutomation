#!/usr/bin/python3
import os, sys

pre="INSERT INTO VportInfo(vportId, mac1, mac2, ipAddr, macAddr, networkId, ipValue, vlanId, subnetId, vportUuid, name, status, networkType, instanceId, targetPoolId, createdTime)"


vportId=100000011
networkId=100000001
subnetId=100000001

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
    #print("hex value = "+hexIpValue)
    #print("hex value to int = "+format(int(hexIpValue, 16)))
    return format(int(hexIpValue, 16))

if __name__ == "__main__":
    args=[]
    if len(sys.argv) < 3:
        sys.exit('not defined argument')
    else:
		for arg in sys.argv : args.append(arg)
        args.pop(0)

    f = open('/root/automation/db_files/sql_script/vports.sql','w')
    stdout = sys.stdout
    sys.stdout = f
    vports=int(args[0])
    ipBefore=args[1]
    cnt=0
    cutIpBefore=ipBefore.split('.')

    while cnt < vports:
        appendIpBefore=str(cutIpBefore[0])+"."+str(cutIpBefore[1])+"."+str(cutIpBefore[2])+"."+ str(cutIpBefore[3])
        #print("first = " + appendIpBefore)
        ipvalue=getIpValue(appendIpBefore)
        #print("ipvalue = "+ipvalue)
        vportUuid = format(int(vportId), '#04x')[2:].upper()
        post=" VALUES("+ str(vportId) +", " +"'"+vportUuid+"'"+ ", 0, " +"'"+ str(cutIpBefore[0])+"."+str(cutIpBefore[1])+ "." + str(cutIpBefore[2]) + "." + str(cutIpBefore[3])+"'"+ ", 'none', " + str(networkId) + ", " + str(ipvalue) + ", -1, " + str(subnetId) +", " +"'"+ vportUuid +"'"+ ", 'none', 'Active', 'F', NULL, NULL, SYSTIMESTAMP);"
        vportId += 1
        tmp=int(cutIpBefore[3])
        tmp+=1
        cutIpBefore[3]=tmp
		appendIpBefore=str(cutIpBefore[0])+"."+str(cutIpBefore[1])+"."+str(cutIpBefore[2])+"."+ str(cutIpBefore[3])
        #print(appendIpBefore)
        cnt += 1
        print(pre+post)

	print("commit;")
    print("exit;")
   	f.close()
  	sys.stdout = stdout
