#!/bin/bash

apt-get -y install nfs-kernel-server nfs-common rpcbind

env1=`grep -r "ZFS_SHARE" /etc/default/zfs`
env2=`grep -r "ZFS_UNSHARE" /etc/default/zfs`

if [ "$env1" == "ZFS_SHARE='no'" ]; then
	sed -i -e "s/ZFS_SHARE='no'/ZFS_SHARE='yes'/g" /etc/default/zfs
else
	echo "ZFS ENV already set"
fi

if [ "$env2" == "ZFS_UNSHARE='no'" ]; then
	sed -i -e "s/ZFS_UNSHARE='no'/ZFS_UNSHARE='yes'/g" /etc/default/zfs
else
	echo "ZFS ENV already set"
fi

if [ -e "/etc/export" ]; then
	echo "ZFS export already set"
else
	touch /etc/export
	echo "/root/tca_agent/zfs_mount   *(rw,fsid=0,insecure,no_subtree_check,async)" > /etc/export
fi
