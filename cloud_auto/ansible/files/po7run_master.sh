#!/bin/bash
echo $PROOBJECT_HOME

sudo /root/jeus8/bin/startDomainAdminServer -domain @@DOMAINNAME@@ -u @@USERNAME@@ -p @@PASSWORDCMD@@ 
sudo /root/jeus8/bin/startManagedServer -dasurl localhost:@@BASE-PORT@@ -domain @@DOMAINNAME@@ -server @@PROOBJECT_SERVER_NAME@@ -u @@USERNAME@@ -p @@PASSWORDCMD@@
sudo /root/jeus8/bin/startManagedServer -dasurl localhost:@@BASE-PORT@@ -domain @@DOMAINNAME@@ -server @@PROOBJECT_SYSMANAGER_SERVER_NAME@@ -u @@USERNAME@@ -p @@PASSWORDCMD@@
sudo /root/jeus8/bin/startManagedServer -dasurl localhost:@@BASE-PORT@@ -domain @@DOMAINNAME@@ -server @@PROOBJECT_TCNM_SERVER_NAME@@ -u @@USERNAME@@ -p @@PASSWORDCMD@@
