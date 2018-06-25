#!/bin/bash


help() {
	echo -e "Usage: ./curl_host_master.sh [OPTIONS] COMMAND"
    echo -e "		./curl_host_master.sh [ --help] \n"
	echo -e "	ex) ./curl_host.sh -n master 1 Portal"
	echo -e "	ex) ./curl_host.sh -e all"
	echo -e "Options: \n"
	echo -e "	-e, --env			Host rack create"
	echo -e "	-n, --name			Host name you should create"
	echo -e "   -h, --help			Print usage\n"
    echo -e "Commands:"
	echo -e "	all				Rack 1,3 all node"
	echo -e "	rack1			Rack 1 all node"
	echo -e "	rack3			Rack 3 all node"
	echo -e "	master	[rack] [Name] 			Master node"
	echo -e "	db		[rack] [Name] 			DB node"
	echo -e "	compute [rack] [Name] 			Compute node"
	echo -e "	storage	[rack] [Name] 			Storage node"
	exit 0
}

## set argument

while getopts "n:-name:e:-env:h:-help" opt
do
	opt="$1"
	case $opt in
		-n | --name) kind="$2" rack="$3" name="$4" node="$5"
		;;
		-e | --env) env="$2"
		;;
		-h | --help) help ;;
		?) help ;;
		*) help ;;
	esac
done

shift $(( $OPTIND -1 ))

log_compute1="/root/automation/170331/host_create/log/demo1/log_compute1"
log_compute3="/root/automation/170331/host_create/log/demo3/log_compute3"
log_storage1="/root/automation/170331/host_create/log/demo1/log_storage1"
log_storage3="/root/automation/170331/host_create/log/demo3/log_storage3"
chostuuid1="/root/automation/170331/host_create/log/demo1/chostuuid"
shostuuid1="/root/automation/170331/host_create/log/demo1/shostuuid"
chostuuid3="/root/automation/170331/host_create/log/demo3/chostuuid"
shostuuid3="/root/automation/170331/host_create/log/demo3/shostuuid"

touch $log_compute1
touch $log_compute3
touch $log_storage1
touch $log_storage3
touch $chostuuid1
touch $shostuuid1
touch $chostuuid3
touch $shostuuid3

rack1_compute_unit() {
curl -X POST -d @cnode1/$name.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts >> $log_compute1
echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@" >> $log_compute1

## extract compute uuid
awk -F: '/uuid/{print $9}' log/demo1/log_compute1 | awk -F '[}]' '{print $1}' | awk -F '["]' '{print $2}' > $chostuuid1
i=1
while read -r line
do
    uuid="$line"
    echo "c_id = $uuid"
    j=$((i+2))
    file_c=cnode1/c1-"$j".json
    echo $file_c

    cp cnode1/cnode.json $file_c
    sed -i -e "s/@@@CHOSTUUID/$uuid/g" $file_c
    sed -i -e "s/@@@CHOSTNAME/Compute1-$i/g" $file_c
    sed -i -e "s/@@@CHOSTDES/Compute1-$j Matching/g" $file_c

    ### ComputeNodeInfo insert
    curl -X POST -d @cnode1/c1-"$j".json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/ComputeNodes >> $log_compute1
    echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@" >> $log_compute1
    ((i++))
done < "$chostuuid1"
exit 0
}

rack3_compute_unit() {

curl -X POST -d @cnode3/$name.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts >> $log_compute3
echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@" >> $log_compute3

awk -F: '/uuid/{print $9}' log/demo3/log_compute3 | awk -F '[}]' '{print $1}' | awk -F '["]' '{print $2}' > $chostuuid3

while read -r line
do
	uuid="$line"
	file_c=cnode3/c3-"$node".json
	cp cnode3/cnode.json $file_c
	sed -i -e "s/@@@CHOSTUUID/$uuid/g" $file_c
	sed -i -e "s/@@@CHOSTNAME/Compute3-$node/g" $file_c
	sed -i -e "s/@@@CHOSTDES/Compute3-$node Matching/g" $file_c

	curl -X POST -d @cnode3/c3-"$node".json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/ComputeNodes >> $log_compute3
	echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@" >> $log_compute3
done < "$chostuuid3"
exit 0
}


rack1_compute() {
## curl Post compute
curl -X POST -d @cnode1/Compute1-5.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts >> $log_compute1
echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@" >> $log_compute1
curl -X POST -d @cnode1/Compute1-6.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts >> $log_compute1
echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@" >> $log_compute1
curl -X POST -d @cnode1/Compute1-7.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts >> $log_compute1
echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@" >> $log_compute1
curl -X POST -d @cnode1/Compute1-8.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts >> $log_compute1
echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@" >> $log_compute1
curl -X POST -d @cnode1/Compute1-9.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts >> $log_compute1
echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@" >> $log_compute1
curl -X POST -d @cnode1/Compute1-10.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts >> $log_compute1
echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@" >> $log_compute1

## extract compute uuid
awk -F: '/uuid/{print $9}' log/demo1/log_compute1 | awk -F '[}]' '{print $1}' | awk -F '["]' '{print $2}' > $chostuuid1
i=1
while read -r line
do
	uuid="$line"
	echo "c_id = $uuid"
	j=$((i+2))
	file_c=cnode1/c1-"$j".json
    echo $file_c

	cp cnode1/cnode.json $file_c
	sed -i -e "s/@@@CHOSTUUID/$uuid/g" $file_c
	sed -i -e "s/@@@CHOSTNAME/Compute1-$i/g" $file_c
	sed -i -e "s/@@@CHOSTDES/Compute1-$j Matching/g" $file_c

	### ComputeNodeInfo insert
	curl -X POST -d @cnode1/c1-"$j".json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/ComputeNodes >> $log_compute1
	echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@" >> $log_compute1
	((i++))
done < "$chostuuid1"
exit 0
}

rack1_storage() {
## curl Post storage
curl -X POST -d @snode1/Storage1-1.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts >> $log_storage1
echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@" >> $log_storage1
curl -X POST -d @snode1/Storage1-2.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts >> $log_storage1
echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@" >> $log_storage1
curl -X POST -d @snode1/Storage1-3.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts >> $log_storage1
echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@" >> $log_storage1

## extract storage uuid
awk -F: '/uuid/{print $9}' log/demo1/log_storage1 | awk -F '[}]' '{print $1}' | awk -F '["]' '{print $2}' > $shostuuid1
i=1
while read -r line
do
	uuid="$line"
	echo "s_id = $uuid"
	file_s=snode1/s1-"$i".json
	echo $file_s

	cp snode1/snode.json $file_s
	sed -i -e "s/@@@SHOSTUUID/$uuid/g" $file_s
	sed -i -e "s/@@@SHOSTNAME/Storage1-$i/g" $file_s
	sed -i -e "s/@@@SHOSTDES/Storage1-$i Matching/g" $file_s

	### StorageNodeInfo insert
	curl -X POST -d @snode1/s1-"$i".json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/StorageNodes >> $log_storage1
	echo "@@@@@@@@@@@@@@@@@@@@@@@@@@" >> $log_storage1
	((i++))
done < "$shostuuid1"
exit0
}

rack3_compute() {
## curl Post compute
curl -X POST -d @cnode3/Compute3-3.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts >> $log_compute3
echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@" >> $log_compute3
curl -X POST -d @cnode3/Compute3-4.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts >> $log_compute3
echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@" >> $log_compute3
curl -X POST -d @cnode3/Compute3-5.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts >> $log_compute3
echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@" >> $log_compute3
curl -X POST -d @cnode3/Compute3-6.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts >> $log_compute3
echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@" >> $log_compute3
curl -X POST -d @cnode3/Compute3-7.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts >> $log_compute3
echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@" >> $log_compute3

## extract compute uuid
awk -F: '/uuid/{print $9}' log/demo3/log_compute3 | awk -F '[}]' '{print $1}' | awk -F '["]' '{print $2}' > $chostuuid3
i=1
while read -r line
do
    uuid="$line"
    echo "c_id = $uuid"
    j=$((i+2))
    file_c=cnode3/c3-"$j".json
    echo $file_c

    cp cnode3/cnode.json $file_c
    sed -i -e "s/@@@CHOSTUUID/$uuid/g" $file_c
    sed -i -e "s/@@@CHOSTNAME/Compute3-$i/g" $file_c
    sed -i -e "s/@@@CHOSTDES/Compute3-$j Matching/g" $file_c

    ### ComputeNodeInfo insert
    curl -X POST -d @cnode3/c3-"$j".json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/ComputeNodes >> $log_compute3
    echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@" >> $log_compute3
    ((i++))
done < "$chostuuid3"

exit 0
}


rack3_storage() {
## curl Post storage
curl -X POST -d @snode3/Storage3-1.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts >> $log_storage3
echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@" >> $log_storage3
curl -X POST -d @snode3/Storage3-2.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts >> $log_storage3
echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@" >> $log_storage3
curl -X POST -d @snode3/Storage3-3.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts >> $log_storage3
echo "@@@@@@@@@@@@@@@@@@@@@@@@@@@@" >> $log_storage3

## extract storage uuid
awk -F: '/uuid/{print $9}' log/demo3/log_storage3 | awk -F '[}]' '{print $1}' | awk -F '["]' '{print $2}' > $shostuuid3
i=1
while read -r line
do
    uuid="$line"
    echo "s_id = $uuid"
    file_s=snode3/s3-"$i".json
    echo $file_s

    cp snode3/snode.json $file_s
    sed -i -e "s/@@@SHOSTUUID/$uuid/g" $file_s
    sed -i -e "s/@@@SHOSTNAME/Storage3-$i/g" $file_s
    sed -i -e "s/@@@SHOSTDES/Storage3-$i Matching/g" $file_s

    ### StorageNodeInfo insert
    curl -X POST -d @snode3/s3-"$i".json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/StorageNodes >> $log_storage3
    echo "@@@@@@@@@@@@@@@@@@@@@@@@@@" >> $log_storage3
    ((i++))
done < "$shostuuid3"
exit 0
}


if [ "$kind" = "master" ]; then
	if [ "$rack" -eq 1 ]; then
		if [ "$name" = "Portal" ]; then
			curl -X POST -d @master1/Portal.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts
		else
			echo "Input wrong name"
		fi
	elif [ "$rack" -eq 3 ]; then
		if [ "$name" = "Portal" ]; then
			curl -X POST -d @master3/Portal.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts
		else
			echo "Input wrong name"
		fi
	else
		echo "Input wrong rack"
	fi
elif [ "$kind" = "db" ]; then
	if [ "$rack" -eq 1 ]; then
		curl -X POST -d @master1/DB.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts
	elif [ "$rak" -eq 3 ]; then
		curl -X POST -d @master3/DB.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts
	fi
elif [ "$kind" = "image" ]; then
	curl -X POST -d @master1/ImageRegistry.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts
elif [ "$kind" = "lb" ]; then
	curl -X POST -d @master1/LB.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts

elif [ "$kind" = "compute" ]; then
	if [ "$rack" -eq 1 ]; then
		rack1_compute_unit
	elif [ "$rack" -eq 3 ]; then
		rack3_compute_unit
	fi
elif [ "$kind" = "storage" ]; then
	if [ "$rack" -eq 1 ]; then
		rack1_storage_unit
	elif [ "$rack" -eq 3 ]; then
		rack3_compute_unit
	fi
fi

if [ "$env" = "all" ]; then
	curl -X POST -d @master1/Portal.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts
	curl -X POST -d @master1/DB.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts
	curl -X POST -d @master1/ImageRegistry.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts
	rack1_compute
	rack1_storage
	curl -X POST -d @master3/Portal.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts
	curl -X POST -d @master3/DB.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts
	curl -X POST -d @master3/ImageRegistry.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts
	rack3_compute
	rack3_storage
elif [ "$env" = "rack1" ]; then
	curl -X POST -d @master1/Portal.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts
    curl -X POST -d @master1/DB.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts
    curl -X POST -d @master1/ImageRegistry.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts
    rack1_compute
    rack1_storage
elif [ "$env" = "rack3" ]; then
	curl -X POST -d @master3/Portal.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts
    curl -X POST -d @master3/DB.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts
    curl -X POST -d @master3/ImageRegistry.json -H "Content-Type: application/json" 172.19.0.3:8081/imp/master/Hosts
    rack3_compute
    rack3_storage
else
	echo "Input wrong env"
fi
