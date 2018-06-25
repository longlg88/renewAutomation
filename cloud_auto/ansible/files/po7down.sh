#!/bin/bash
/root/jeus8/bin/stopNodeManager -host localhost -port 7730
/root/jeus8/bin/stopServer -host localhost:19736 -u jeus -p jeus
/root/jeus8/bin/stopServer -host localhost:24736 -u jeus -p jeus
/root/jeus8/bin/stopServer -host localhost:14736 -u jeus -p jeus
/root/jeus8/bin/stopServer -host localhost:9736 -u jeus -p jeus
