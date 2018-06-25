#!/bin/bash
../jeus8/bin/stopNodeManager -host localhost -port 7730
../jeus8/bin/stopServer -host localhost:19736 -u jeus -p jeus
../jeus8/bin/stopServer -host localhost:9736 -u jeus -p jeus
