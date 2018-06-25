#!/bin/bash

chmod +x /etc/init.d/tca-image-scp

update-rc.d tca-image-scp defaults
update-rc.d tca-image-scp enable
