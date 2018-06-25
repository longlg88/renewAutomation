#!/bin/bash

echo >> /etc/profile
echo HISTTIMEFORMAT=\"[%Y-%m-%d-%H:%M:%S] \" >> /etc/profile 
echo export HISTTIMEFORMAT >> /etc/profile


mv /sbin/shutdown /sbin/shutdown-backup
echo >> /etc/bash.bashrc

echo alias shutdown=\"echo You are not allowed to use this command \" >> /etc/bash.bashrc
