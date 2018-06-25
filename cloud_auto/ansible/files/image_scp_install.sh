#!/bin/bash

# Package Install
apt-get install -y openssh-server openssh-client
apt-get install -y sshpass
apt-get install -y curl
DEBIAN_FRONTEND=noninteractive apt-get install -y procmail
