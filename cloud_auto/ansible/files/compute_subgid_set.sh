#!/bin/bash

echo root:0:65536 > /etc/subuid
/bin/bash -c 'rm -f /etc/subgid; for i in {1..5000..1}; do echo "root:$(expr $i \* 100000):65536" >> /etc/subgid; done;'
