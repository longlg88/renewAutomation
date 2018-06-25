#!/bin/bash

touch /root/automation/ssd.sh;
touch /root/automation/hdd.sh;

# get root device
export rootDev=$(mount | grep  -Po "/dev/(.*)[0-9] on / type" | perl -pe 's/\/dev\/(.*)[0-9] on \/ .*/$1/');
if ! echo $rootDev | grep ".d[a-z]$" >& /dev/null; then echo "error: no rootDev" >&2; exit 1; fi

# print list
h_num=-1
s_num=0
dev_num=1
devarray=()
ssdarray=()
export rootDev=$(mount | grep  -Po "/dev/(.*)[0-9] on / type" | perl -pe 's/\/dev\/(.*)[0-9] on \/ .*/$1/');
for dev in $(lsblk | grep disk | awk '{print $1}');
do
echo $dev
   if [ "$rootDev" != "$dev" ]; then
       if [ $(cat /sys/block/$dev/queue/rotational) == 1 ]; then
           echo "## create /dev/$dev" >> /root/automation/hdd.sh
           echo "pvcreate -f /dev/$dev" >> /root/automation/hdd.sh
           if [ $h_num -ge 0 ]; then
               devarray[$h_num]="/dev/$dev"
               h_num=$((h_num+1))
           else
               echo "vgcreate hd_conatiner_vg /dev/$dev" >> /root/automation/hdd.sh
               echo "lvcreate -n hd_container_data -L @@stg_hdd_container_lvm_size@@ hd_container_vg" >> /root/automation/hdd.sh
               echo "mkfs.xfs -f /dev/hd_container_vg/hd_container_data" >> /root/automation/hdd.sh
               echo "/dev/$dev$dev_num /root/tca_agent xfs defaults,pquota 0 1" >> /etc/fstab
               h_num=$((h_num+1)) 
           fi
       else
           echo "pvcreate -f /dev/$dev" >> /root/automation/ssd.sh
           ssdarray[$s_num]="/dev/$dev"
           s_num=$((s_num+1))
       fi
   fi
done

### db setting

hdd_count=${#devarray[*]}
ssd_count=${#ssdarray[*]}
### ceph setting
ceph_ssdarray=()
for i in {0..2}
do
    ceph_ssdarray[$i]=${ssdarray[$i]}
done

echo "vgcreate ceph_wal_vg ${ceph_ssdarray[*]}" >> /root/automation/ssd.sh
echo "vgcreate ceph_data_vg ${devarray[*]}" >> /root/automation/hdd.sh

echo "lvcreate -n ceph_data1 -L @@stg_hdd_lvm_size@@ ceph_data_vg" >> /root/automation/hdd.sh
echo "lvcreate -n ceph_data2 -L @@stg_hdd_lvm_size@@ ceph_data_vg" >> /root/automation/hdd.sh
echo "lvcreate -n ceph_data3 -L @@stg_hdd_lvm_size@@ ceph_data_vg" >> /root/automation/hdd.sh
echo "lvcreate -n ceph_wal1 -L @@stg_ssd_lvm_size@@ ceph_wal_vg" >> /root/automation/ssd.sh
echo "lvcreate -n ceph_wal2 -L @@stg_ssd_lvm_size@@ ceph_wal_vg" >> /root/automation/ssd.sh
echo "lvcreate -n ceph_wal3 -L @@stg_ssd_lvm_size@@ ceph_wal_vg" >> /root/automation/ssd.sh


### db setting
db_ssdarray=()
cnt=0
for i in {3..9}
do
    db_ssdarray[$cnt]=${ssdarray[$i]}
    cnt=`expr $cnt\+1`
done
echo "vgcreate hd_db_vg ${db_ssdarray[*]}" >> /root/automation/ssd.sh
echo "lvcreate -n hd__dbdata_vg -L @@db_ssd_lvm_size@@ hd_db_vg" >> /root/automation/ssd.sh
echo "mkfs.xfs -f /dev/hd_db_vg/hd_dbdata_vg" >> /root/automation/ssd.sh
echo "/dev/hd_db_vg/hd_dbdata_vg /mnt/tca_agent/xfs_mount xfs defaults,pquota 0 1" >> /etc/fstab




chmod 755 /root/automation/ssd.sh
chmod 755 /root/automation/hdd.sh

