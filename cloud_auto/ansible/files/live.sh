#!/bin/bash

cd /root/sys_agent
ip=`ip addr | grep "inet " | grep brd | awk '{print $2}' | awk -F/ '{print $1}' | sed -n 2p`
if [ -z "$ip" ]; then
    ip=`ip addr | grep "inet " | grep brd | awk '{print $2}' | awk -F/ '{print $1}'`
fi
touch -c $ip
live=`pgrep -c sysmanageragent`
echo $live > "$ip"
