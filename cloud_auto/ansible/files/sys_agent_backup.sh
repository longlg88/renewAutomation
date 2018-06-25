#!/bin/bash
source /root/sys_agent/setenv

cd /root/sys_agent

lxc_container_list=`lxc-ls --running`
for lxc_container in $lxc_container_list;do
        gresult=`grep -r "lxc.cgroup.cpu.share" /root/tca_agent/container_config/$lxc_container`
        IFS=' ' read -r -a array <<< "$gresult"
        cont_cpu=${array[2]}
        cont_cpu=$((cont_cpu/1024))
        project_id=`cat $HOME/sys_agent/idmaps/$lxc_container | awk '{print $1}'`
        tenant_id=`cat $HOME/sys_agent/idmaps/$lxc_container | awk '{print $2}'`
        /root/sys_agent/notify_sysmanager_agent --action create --type lxc --id $lxc_container --cores $cont_cpu --project $project_id --tenant $tenant_id
        gresult=`grep -r "lxc.network.veth.pair" /root/tca_agent/container_config/$lxc_container`
        iter_num=1
        for veth in $gresult;do
                it=$((iter_num%3))
                if [ $it -eq 0 ];then
                        /root/sys_agent/notify_sysmanager_agent --action attach-nic --id $lxc_container --nic-id $veth
                fi
                iter_num=$((iter_num=iter_num+1))
        done
done
