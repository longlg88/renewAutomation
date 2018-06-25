#!/bin/bash

# Package Install
sudo apt-get install -y openssh-server openssh-client
sudo apt-get install -y sshpass
sudo apt-get install -y curl
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y procmail
