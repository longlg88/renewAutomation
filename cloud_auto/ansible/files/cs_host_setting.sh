#!/bin/bash

chmod +x /etc/init.d/tca-compute

update-rc.d tca-compute defaults
update-rc.d tca-compute enable
