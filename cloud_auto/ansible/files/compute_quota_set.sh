#!/bin/bash

mount -o remount,rw,grpquota /
quotacheck -cvgmf /
quotaon /

## check quota

# repquota -g /
