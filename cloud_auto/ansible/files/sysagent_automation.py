#!/usr/bin/env python

from docopt import docopt
import sys
import os
import subprocess
import shutil

def getOriginalFilesDirectory(path):
    # print path
    #home=os.getenv('user_home')
    #mergedPath = path + home+'/sys_agent/'
    mergedPath = path + '/root/sys_agent/'
    # print 'mergedpath is: ', mergedPath
    return mergedPath

def getStagingDirectory():
    return './sysagentlogs'

def moveFileToStaging(path, name, postfix):
    targetFilePath = os.path.join(path, name)
    # print 'targetFilePath: ', targetFilePath
    # print 'path: ', path
    # print 'name: ', name
    # print 'postfix: ', postfix
    newFileName = os.path.join(getStagingDirectory(), name + '-' + postfix)
    # print newFileName
    shutil.move(targetFilePath, newFileName)

def collectLive(rootDirectory, source):
    # print rootDirectory
    # print getOriginalFilesDirectory(rootDirectory)
    for root, dirs, files in os.walk(getOriginalFilesDirectory(rootDirectory)):
        for item in files:
            # print item
            if item == 'live':
                #print 'collecting'
                # print 'filepath: ', targetFilePath
                moveFileToStaging(root, item, source)

def printLive():
    for root, dirs, files in os.walk(getStagingDirectory()):
        for item in files:
            if item.startswith('live'):
                print "here"
                livefile = open(os.path.join(root, item), 'r')
                filecontents = livefile.readline().strip()
                # print "<", filecontents, ">"
                if filecontents == '1':
                    print item, " On"
                elif filecontents == '0':
                    print item, " Off"
                else:
                    print item, " Unknown"


# [--directory=<directory>]
# --directory=path  Set working directory [default: ./sysagentlogs]

optString = """Usage: sysagent_automation.py [options] [--sendto=<address>]

Moves all directories starting with "172.31.*" to ./sysagentlogs
(if --directory unspecified) and then operates on them.

--clean      Clean all previously received files and directories
--deploy     Deploy to proxy node
--live       Show agent liveness status
--core       Specify output file [default: ./test.txt]
--log        Print less text
--sendto=IP     Host to send data to. Needed for --core and --log

"""

options = docopt(optString, sys.argv[1:])

# print options
clean = options["--clean"]
deploy = options["--deploy"]
live = options["--live"]
core = options["--core"]
log = options["--log"]
sendto = options["--sendto"]

if deploy:
    subprocess.call('scp sysagent_automation.py docopt.py sshroot@175.195.163.11:'+home+'/automation', shell=True)
    exit(0)

if core or log:
    if not sendto:
        print("sendto must be specified!")
        exit(1)
# else:
#     if not live:
#         print()

for root, dirs, files in os.walk("./"):
    for dir in dirs:
        if not dir.startswith("192"):
           continue
        # print(dir)
        targetDir = os.path.join('./', dir)
        if live:
            collectLive(targetDir, dir)
        if core:
            collectCore(targetDir, dir)
        if log:
            collectLog(targetDir, dir)
        if clean:
            print "Delete: ", targetDir
            shutil.rmtree(targetDir)

if live:
    printLive()
if core or log:
    sendToDestination()
