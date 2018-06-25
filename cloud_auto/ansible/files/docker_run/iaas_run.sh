#!/bin/bash

image_tag=`docker images | awk '/$master_name/{print $2}'`

image_id=`docker ps | awk '/$master_name/{print $2}'`
if [ "$image_id" = "$master_name":"$image_tag" ]; then
    echo "same docker container runs here"
else
    docker run -d --name=$app_name -p $outbound_port1:6776 -p $outbound_port2:9008 -p $webadmin_port:9736 -p $http_port:8080 -v $po7_path:/root/proobject7 -e PO7_RUNTIME_WAR=$po7_runtime_war -e TIBERO_IP=$db_ip -e TIBERO_USER=$db_user -e TIBERO_PW=$db_password -e TIBERO_PORT=$db_port -it $master_name:$image_tag
fi
