#!/bin/bash

sudo service docker stop

cd $HOME/automation/initial/docker_binary

tar -xvf ../docker_binary.tar

mv /usr/bin/docker /usr/bin/docker_org
mv /usr/bin/dockerd /usr/bin/dockerd_org

#cp $HOME/automation/initial/docker_ce_binary/docker-linux-amd64 /usr/bin/docker
#cp $HOME/automation/initial/docker_ce_binary/dockerd-dev /usr/bin/dockerd

ln -s $HOME/automation/initial/docker_binary/docker_ce_binary/docker-linux-amd64 /usr/bin/docker
ln -s $HOME/automation/initial/docker_binary/docker_ce_binary/dockerd-dev /usr/bin/dockerd

cp $HOME/automation/initial/docker_binary/docker_ce_binary/docker-runc /usr/bin/docker-runc
cp $HOME/automation/initial/docker_binary/docker_ce_binary/docker-proxy /usr/bin/docker-proxy
cp $HOME/automation/initial/docker_binary/docker_ce_binary/docker-containerd /usr/bin/docker-containerd
cp $HOME/automation/initial/docker_binary/docker_ce_binary/docker-containerd-ctr /usr/bin/docker-containerd-ctr
cp $HOME/automation/initial/docker_binary/docker_ce_binary/docker-containerd-shim /usr/bin/docker-containerd-shim

sudo service docker start
