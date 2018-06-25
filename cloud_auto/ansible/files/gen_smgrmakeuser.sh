#!/bin/bash

if [ -f $PWD/automation/db_files/sql_script/sm7event_makeuser.sql ]; then
    echo "skip generate"
    exit
else
    touch $PWD/automation/db_files/sql_script/sm7event_makeuser.sql
    touch $PWD/automation/db_files/sql_script/smgr_makeuser.sql
fi

sm7sql=$PWD/automation/db_files/sql_script/sm7event_makeuser.sql
smgrsql=$PWD/automation/db_files/sql_script/smgr_makeuser.sql

echo "create user $SMEVENTID identified by '$SMEVENTPW';" >> $sm7sql
echo "grant create sequence to $SMEVENTID;" >> $sm7sql
echo "grant create table to $SMEVENTID;" >> $sm7sql
echo "grant create session to $SMEVENTID;" >> $sm7sql
echo "grant create trigger to $SMEVENTID;" >> $sm7sql

echo "commit;" >> $sm7sql
echo "exit;" >> $sm7sql

echo "CREATE TABLESPACE $tablespace_name DATAFILE '/root/tibero6/database/tibero/"$tablespace_name"001.dtf' SIZE 10G AUTOEXTEND ON NEXT 10G EXTENT MANAGEMENT LOCAL UNIFORM SIZE 256K;" >> $smgrsql

echo "create user $SMGRID identified by '$SMGRPW' DEFAULT TABLESPACE $tablespace_name;" >> $smgrsql
echo "grant create sequence to $SMGRID;" >> $smgrsl
echo "grant create table to $SMGRID;" >> $smgrsql
echo "grant create session to $SMGRID;" >> $smgrsql
echo "grant create trigger to $SMGRID;" >> $smgrsql

echo "commit;" >> $smgrsql
echo "exit;" >> $smgrsql
