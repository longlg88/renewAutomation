#!/bin/bash

grep -r "net.core" /etc/sysctl.conf

if [ $? = 1 ]; then
        echo "net.core.rmem_default=262144" >> /etc/sysctl.conf
        echo "net.core.wmem_default=262144" >> /etc/sysctl.conf
        echo "net.core.rmem_max = 33554432" >> /etc/sysctl.conf
        echo "net.core.wmem_max = 33554432" >> /etc/sysctl.conf
        echo "fs.aio-max-nr = 1048576" >> /etc/sysctl.conf
        sysctl -p
else
        echo "sys parameter already modify"
fi
