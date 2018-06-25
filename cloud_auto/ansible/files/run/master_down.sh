#!/bin/bash

export JEUS_HOME=@@jeus_home@@
export PATH=$JEUS_HOME/bin:$JEUS_HOME/lib/system:$PATH
export PROOBJECT_HOME=/root/po7/

$JEUS_HOME/bin/stopNodeManager -host localhost -port @@totalmaster_nodemanager_port@@
$JEUS_HOME/bin/stopServer -host localhost:@@po_base_port@@ -u @@USERNAME@@ -p @@PASSWORDCMD@@
$JEUS_HOME/bin/stopServer -host localhost:@@po_sysmanager_base_port@@ -u @@USERNAME@@ -p @@PASSWORDCMD@@
$JEUS_HOME/bin/stopServer -host localhost:@@po_cds_base_port@@ -u @@USERNAME@@ -p @@PASSWORDCMD@@
$JEUS_HOME/bin/stopServer -host localhost:@@BASE-PORT@@ -u @@USERNAME@@ -p @@PASSWORDCMD@@
