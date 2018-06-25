#!/bin/bash

sudo /root/jeus8/bin/startDomainAdminServer -domain @@DOMAINNAME@@ -u @@USERNAME@@ -p @@PASSWORDCMD@@ 
sudo /root/jeus8/bin/startManagedServer -dasurl localhost:@@BASE-PORT@@ -domain @@DOMAINNAME@@ -server @@PROOBJECT_SERVER_NAME@@ -u @@USERNAME@@ -p @@PASSWORDCMD@@
sudo /root/jeus8/bin/startNodeManager &
