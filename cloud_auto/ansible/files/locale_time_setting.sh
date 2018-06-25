#!/bin/bash

## time setting
sudo timedatectl set-timezone Asia/Seoul

## locale setting
find_locale=`cat /etc/default/locale | grep "LANG=" | sed -e 's/"//g' | awk -F= '{ print $2 }'`
if [ "$find_locale" != "$locale" ]; then
    sudo sed -i "s/en_US.UTF-8/$locale/g" /etc/default/locale
else
    echo "don't need to change locale.. this locale is $locale"
fi

## history setting
sudo echo 'HISTTIMEFORMAT="[%Y-%m-%d-%H:%M:%S] "' >> /etc/profile
sudo echo 'export HISTTIMEFORMAT' >> /etc/profile
sudo source /etc/profile
