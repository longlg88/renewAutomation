#!/bin/bash

source /root/sys_agent/setenv

cd /root/sys_agent

./sysmgr-agent --agent-id $TMAX_CLOUD_NODE_ID --sysmgr-ip $TMAX_SYSMANAGER_IP --sysmgr-port $TMAX_SYSMANAGER_PORT
