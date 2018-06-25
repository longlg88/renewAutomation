
#!/bin/bash
help() {
    echo -e "Usage: ./ansible.sh [OPTIONS] COMMAND"
    echo -e "       ./ansible.sh [ --help] \n"
    echo -e "Options: \n"
    echo -e "     -h            Print usage\n"
    echo -e "     -o            Choose apt-get install ansible or deb install ansible"
    echo -e "     -o            y / n"
    exit 0
}

while getopts "o:h:-help" opt
do
    case $opt in
        o ) aptInstall="$2" ;;
        h ) help ;;
        -help ) help ;;
        ? ) help ;;
        * ) help ;;
    esac
done
if [ $OPTIND -eq 1 ]; then
    help
fi
shift $(( $OPTIND -1 ))

if [ "$aptInstall" == "y" ]; then
    sudo apt-get -y update
    sudo apt-get -y upgrade
    sudo apt-get -y install python3 expect
    sudo apt-get -y install python-pip3
    sudo pip3 install paramiko pyyaml
    sudo apt-get -y install software-properties-common
    sudo apt-add-repository ppa:ansible/ansible -y
    sudo apt-get -y update
    sudo apt-get -y install ansible
    cd $PWD/ansible/
    cp ansible.cfg /etc/ansible/ansible.cfg
else
    cd $PWD/install_ansible/software-properties-common/
    sudo sh install.sh
    cd $PWD/install_ansible/python/
    sudo sh install.sh
    cd $PWD/install_ansible/ansible-2.4.0/
    sudo sh install.sh
    mkdir /usr/local/lib/python3.5
    mkdir /usr/local/lib/python3.5/dist-packages/
    cd $PWD/install_ansible/
    cp -r python3-packages/ /usr/local/lib/python3.5/dist-packages/
    cd $PWD/config/
    cp ansible.cfg /etc/ansible/ansible.cfg
    cd $PWD/config/
    cp value_info $PWD/ansible/files/initial_value_setting/
fi
