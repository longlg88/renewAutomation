#!/bin/bash

source /root/sys_agent/setenv

cd /root/sys_agent

filename="/root/sys_agent/log"

if [ -f "$filename" ]; then
    mv /root/sys_agent/log /root/sys_agent/log$(date +\%m\%d\%H\%M)
    touch /root/sys_agent/manage_log
    echo -n "generation time : " >> /root/sys_agent/manage_log
    nohup ./sysmanageragent > /root/sys_agent/log  &
else
    nohup ./sysmanageragent > /root/sys_agent/log  &
fi
