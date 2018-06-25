#!/bin/bash

if [ -f $PWD/automation/db_files/sql_script/make_csvmgruser.sql ]; then
    echo "skip generate"
    exit
else
    touch $PWD/automation/db_files/sql_script/make_csvmgruser.sql
fi

sql=$PWD/automation/db_files/sql_script/make_csvmgruser.sql

echo "create user $CSVMGR_META_DB_USER identified by '$CSVMGR_META_DB_PWD';" >> $sql
echo "grant create sequence to $CSVMGR_META_DB_USER;" >> $sql
echo "grant create session to $CSVMGR_META_DB_USER;" >> $sql
echo "grant create table to $CSVMGR_META_DB_USER;" >> $sql
echo "grant create trigger to $CSVMGR_META_DB_USER;" >> $sql

echo "commit;" >> $sql
echo "exit;" >> $sql
