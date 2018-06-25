#!/bin/bash

touch /root/automation/hdd.sh;

# get root device
export rootDev=$(mount | grep  -Po "/dev/(.*)[0-9] on / type" | perl -pe 's/\/dev\/(.*)[0-9] on \/ .*/$1/');
if ! echo $rootDev | grep ".d[a-z]$" >& /dev/null; then echo "error: no rootDev" >&2; exit 1; fi

# print list
num=0
devarray=()
export rootDev=$(mount | grep  -Po "/dev/(.*)[0-9] on / type" | perl -pe 's/\/dev\/(.*)[0-9] on \/ .*/$1/');
for dev in $(lsblk | grep disk | awk '{print $1}');
do
echo $dev
   if [ "$rootDev" != "$dev" ]; then
       if [ $(cat /sys/block/$dev/queue/rotational) == 1 ]; then
           echo "pvcreate -f /dev/$dev" >> /root/automation/hdd.sh
           devarray[$num]="/dev/$dev"
#       else
#           echo /dev/$dev >> /root/ssd.ssh
       fi
       num=`expr $num\+1`
   fi
done

echo "vgcreate hd_vg ${devarray[*]}" >> /root/automation/hdd.sh

echo "lvcreate -n hd_data_vg -L @@com_lvm_size@@ hd_vg" >> /root/automation/hdd.sh

echo "mkfs.xfs -f /dev/hd_vg/hd_data_vg" >> /root/automation/hdd.sh

chmod 755 /root/automation/hdd.sh

echo "/dev/hd_vg/hd_data_vg /root/tca_agent xfs defaults,pquota 0 1" >> /etc/fstab
