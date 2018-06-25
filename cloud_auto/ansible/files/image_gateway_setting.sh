#!/bin/bash

sudo update-rc.d tca-agent remove

sudo rm -f /etc/init.d/tca-agent


sudo chmod +x /etc/init.d/tca-image-gateway

sudo update-rc.d tca-image-gateway defaults
sudo update-rc.d tca-image-gateway enable
