#!/bin/bash

# Package Install
apt-get install -y openssh-server
apt-get install -y openssh-client
apt-get install -y sshpass
apt-get install -y net-tools
apt-get install -y bridge-utils
apt-get install -y arptables
apt-get install -y iproute
apt-get install -y iproute2
apt-get install -y curl
apt-get install -y nfs-common
DEBIAN_FRONTEND=noninteractive apt-get install -y procmail
apt-get install -y socat
apt-get install -y websockify

## Container
apt-get install -y lxc

## VM
apt-get install -y expect
apt-get install -y qemu-kvm
apt-get install -y genisoimage
apt-get install -y cloud-utils
apt-get install -y openvpn

## Quota
apt-get install -y quota
