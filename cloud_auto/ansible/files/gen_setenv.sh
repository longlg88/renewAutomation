#!/bin/bash

home=$PWD
echo $home

if [ -f $home/automation/db_files/setenv ]; then
    echo "skip generate"
    exit
else
    touch $home/automation/db_files/setenv
fi

setenv=$home/automation/db_files/setenv

echo "#!/bin/bash" >> $setenv
echo "export TB_HOME=$TB_HOME" >> $setenv
echo "export TB_SID=$TB_SID" >> $setenv
echo 'export LD_LIBRARY_PATH=$TB_HOME/lib:$TB_HOME/client/lib' >> $setenv
echo 'export PATH=$PATH:$TB_HOME/bin:$TB_HOME/client/bin' >> $setenv

echo "#################### tb home add #########################" >> $home/.profile
echo "export TB_HOME=$TB_HOME" >> $home/.profile
echo "export TB_SID=$TB_SID" >> $home/.profile
echo 'export LD_LIBRARY_PATH=$TB_HOME/lib:$TB_HOME/client/lib' >> $home/.profile
echo 'export PATH=$PATH:$TB_HOME/bin:$TB_HOME/client/bin' >> $home/.profile
echo "#################### tb home end #########################" >> $home/.profile
