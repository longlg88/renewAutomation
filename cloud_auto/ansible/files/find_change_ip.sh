#!/bin/bash

## find IP
host_ip=`ifconfig $SETTING_INTERFACE | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}'` > log

## Change IP
sed -i -e "s/@@SETTING_IP/$host_ip/g" $HOME/automation/gen_iaaslite.sh
