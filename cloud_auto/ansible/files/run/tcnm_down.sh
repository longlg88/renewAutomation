#!/bin/bash

export JEUS_HOME=@@jeus_home@@
export PATH=$JEUS_HOME/bin:$JEUS_HOME/lib/system:$PATH
export PROOBJECT_HOME=/root/proobject7


$JEUS_HOME/bin/stopServer -host localhost:@@po_tcnm_base_port@@ -u @@USERNAME@@ -p @@PASSWORDCMD@@
$JEUS_HOME/bin/stopServer -host localhost:@@BASE-PORT@@ -u @@USERNAME@@ -p @@PASSWORDCMD@@
