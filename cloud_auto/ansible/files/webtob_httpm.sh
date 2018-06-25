#!/bin/bash
export JAVA_HOME=/usr/java8_64
export WEBTOBDIR=/root/webtob
export PATH=$JAVA_HOME/bin:$WEBTOBDIR/bin:$PATH
export LD_LIBRARY_PATH=$WEBTOBDIR/lib

wscfl -i /root/webtob/config/http.m
