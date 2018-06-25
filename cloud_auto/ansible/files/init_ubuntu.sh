#!/bin/bash

# apt update && upgrade && remove unnecessary files
echo -e "apt update && upgrade && remove unnecessary files"
apt-get -y update
apt-get -y upgrade


# apt install vim
echo -e "apt install vim"
apt-get -y install vim
apt-get -y install python3-pip
pip3 install paramiko
pip3 install pycrypto
pip3 install pyyaml

apt-get -y install sshpass
