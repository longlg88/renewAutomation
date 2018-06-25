#!/bin/bash

export JEUS_HOME=@@jeus_home@@
export PATH=$JEUS_HOME/bin:$JEUS_HOME/lib/system:$PATH
export PROOBJECT_HOME=/root/po7/

$JEUS_HOME/bin/stopServer -host localhost:@@po_sysmanager_base_port@@ -u @@USERNAME@@ -p @@PASSWORDCMD@@

$JEUS_HOME/bin/startManagedServer -dasurl localhost:@@BASE-PORT@@ -domain @@DOMAINNAME@@ -server @@PROOBJECT_SYSMANAGER_SERVER_NAME@@ -u @@USERNAME@@ -p @@PASSWORDCMD@@

