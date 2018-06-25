#!/bin/bash
home=$PWD
echo $home

if [ -f $home/sys_agent/setenv ]; then
    echo "skip generate"
    exit
else
    touch $home/sys_agent/setenv
fi

setenv=$home/sys_agent/setenv
host=$home/sys_agent/host

FILE=$home/sys_agent/file_for_sysmanageragent

while read host_ip host_id
do
	if [ $host_ip == "@@host_ip@@" ]; then
		id=`printf '%08x' $host_id`
	fi
done < $FILE
#current_ip=`ifconfig eno2 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}'`
#curl -X GET "http://"+$master_ip+":8080/imp/master/Hosts?action=List&offset=0&limit=1&q=hostIp='$current_ip'" > $res
#ip=`awk -F, '{print $5}' $res | awk -F: '{print $2}' | awk -F'"' '{print $2}'`

#echo $current_ip
#echo $ip

#if [ "$ip" = "$current_ip" ]; then
#	uuid=`awk -F, '/hostUuid/{print $3}' $res | awk -F: '{print $2}' | awk -F'"' '{print $2}'`
#else
#	echo "IP matching is wrong"
#fi

echo "#!/bin/bash" >> $setenv
echo "export TMAX_SYSMANAGER_PORT=$TMAX_SYSMANAGER_PORT" >> $setenv
echo "export TMAX_SYSMANAGER_IP=$TMAX_SYSMANAGER_IP" >> $setenv
echo "export TMAX_SYSMANAGER_AGENT_PORT=$TMAX_SYSMANAGER_AGENT_PORT" >> $setenv
echo "export TMAX_CLOUD_NODE_ID=$id" >> $setenv
echo "export TMAX_SYSMANAGER_AGENT_ANYMINER_PORT=$TMAX_SYSMANAGER_AGENT_ANYMINER_PORT" >> $setenv
echo "export TMAX_SYSMANAGER_AGENT_ANYMINER_IP=$TMAX_SYSMANAGER_AGENT_ANYMINER_IP" >> $setenv
echo "export TMAX_SYSMANAGER_AGENT_CONTAINER_RW_LAYER_DIRECTORY=$TMAX_SYSMANAGER_AGENT_CONTAINER_RW_LAYER_DIRECTORY" >> $setenv
echo "export TMAX_SYSMANAGER_AGENT_HOST_INTERFACE=$TMAX_SYSMANAGER_AGENT_HOST_INTERFACE" >> $setenv
echo "export TMAX_SYSMANAGER_AGENT_REPORT_LOCATION=$TMAX_SYSMANAGER_AGENT_REPORT_LOCATION" >> $setenv
echo "export TMAX_SYSMANAGER_AGENT_QEMU_IMAGE_FILE_DIRECTORY=$TMAX_SYSMANAGER_AGENT_QEMU_IMAGE_FILE_DIRECTORY" >> $setenv
