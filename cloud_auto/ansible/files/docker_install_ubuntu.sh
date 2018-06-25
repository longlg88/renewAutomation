#!/bin/bash

echo "start docker install"


sudo add-apt-repository "deb https://apt.dockerproject.org/repo/ ubuntu-$(lsb_release -cs) main"

sudo apt-get -y install apt-transport-https ca-certificates curl software-properties-common

sudo curl -fsSL https://apt.dockerproject.org/gpg | sudo apt-key add -

sudo apt-get -y update

sudo apt-get -y install docker-engine
