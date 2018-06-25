#!/bin/bash

search=/root/netplan

for LINE in `ls $searchdir`
do
	filename=`basename $LINE.yaml`
done

file=$search/$filename
echo $file
