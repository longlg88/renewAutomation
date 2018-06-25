#!/bin/bash

ifconfig eno1 0
ifconfig eno1 down
netplan apply
sleep 1
