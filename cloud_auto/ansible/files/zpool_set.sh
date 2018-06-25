#!/bin/bash

lines=`zpool list | awk "{print NR}" `

echo "$lines"

for i in $lines
do
	if [ $i -ge 2 ]
	then
		flag=true
		echo "$flag"
		break
	else
		flag=false
		echo "$flag"
	fi
done


if [ $flag = "false" ]
then
	`zpool create -f $ZPOOL raidz $VOLUME1 $VOLUME2 $VOLUME3`
fi
