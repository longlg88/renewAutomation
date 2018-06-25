#!/bin/bash

id=`pgrep sysmanageragent`

if [ $id ]; then
    echo "pid = $id"
    kill -9 $id
else
    echo "there is no sysmanager agent pid"
fi
