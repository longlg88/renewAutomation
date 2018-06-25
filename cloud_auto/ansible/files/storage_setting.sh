#!/bin/bash

update-rc.d tca-agent remove

chmod +x /etc/init.d/tca-storage

update-rc.d tca-storage defaults
update-rc.d tca-storage enable
