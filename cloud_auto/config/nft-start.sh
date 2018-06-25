#!/bin/bash

# init script for compute node with sdn.
# by jungsub_shin

### BEGIN INIT INFO
# Provides:          tca-compute
# Required-Start:        $network $remote_fs
# Required-Stop:     $network $remote_fs
# Default-Start:         2 3 4 5
# Default-Stop:      0 1 6
### END INIT INFO

interface="enp2s0"
index=11
end=$((index+29))


# Run
case "$1" in
  start)
        while :
        do
                ifconfig ${interface}:$index 192.168.60.$index/24
                index=$((index + 1))
                if [ ${index} -eq ${end} ]; then
                        break
                fi
        done
        route add -net 172.20.0.0 netmask 255.255.255.0 gw 172.16.0.2
        nft -f /root/nft_file/rule
        ;;
 restart|reload|force-reload)
        echo "Error: argument '$1' not supported" >&2
        echo "Usage: $0 [start|stop]" >&2
        exit 3
        ;;
  stop|"")
;;
  *)
        echo "Usage: $0 [start|stop]" >&2
        exit 3
        ;;
esac
