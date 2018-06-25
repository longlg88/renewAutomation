#!/bin/bash

export JEUS_HOME=@@jeus_home@@
export PATH=$JEUS_HOME/bin:$JEUS_HOME/lib/system:$PATH
export PROOBJECT_HOME=/root/proobject7

$JEUS_HOME/bin/startDomainAdminServer -domain @@DOMAINNAME@@ -u @@USERNAME@@ -p @@PASSWORDCMD@@

$JEUS_HOME/bin/startManagedServer -dasurl localhost:@@BASE-PORT@@ -domain @@DOMAINNAME@@ -server @@PROOBJECT_TCNM_SERVER_NAME@@ -u @@USERNAME@@ -p @@PASSWORDCMD@@
