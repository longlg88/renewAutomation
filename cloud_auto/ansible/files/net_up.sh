#!/bin/bash

vconfig add eno1 2
vconfig add eno1 3

service networking restart
sleep 1
