import subprocess
import os
import shutil
import sys
from glob import glob

sys.path.insert(0,'config/')
import gvar

def init_essential():
    result=subprocess.Popen(['sudo dpkg -l ansible'],shell=True, stdout=subprocess.PIPE)
    data=result.communicate()[0]
    pwd=os.getcwd()
    if not data.decode('utf-8'):
        print("(1) install ansible using apt-get (2) install ansible using deb (q) quit")
        input_result=input()
        if(input_result == "1"):
            try:
                result = subprocess.run(['sudo', 'apt-get','update'])
                result = subprocess.run(['sudo', 'apt-get','upgrade','-y'])

                result = subprocess.run(['sudo', 'apt-get','install','python-pip','-y'])
                result = subprocess.run(['sudo', 'apt-get','install','python-pip3','-y'])
                result = subprocess.run(['sudo', 'apt-get','install','expect','-y'])

                result = subprocess.run(['sudo', 'pip3','install','paramiko'])
                result = subprocess.run(['sudo', 'pip3','install','pyyaml'])

            except Exception as e:
                print(type(e).__name__)

            install_ansible_apt()
        elif(input_result == "2"):
            result = subprocess.run('./install_ansible/software-properties-common/install.sh',shell=True)
            result = subprocess.run('./install_ansible/python/install.sh',shell=True)
            result = subprocess.run('./install_ansible/ansible-2.4.0/install.sh',shell=True)
            if (os.path.exists('/usr/local/lib/python3.5') == False):
                result = subprocess.run(['mkdir','/usr/local/lib/python3.5'])
                result = subprocess.run(['mkdir','/usr/local/lib/python3.5/dist-packages/'])
        
            result = subprocess.run(['cp','-r',pwd+'/install_ansible/python3-packages/','/usr/local/lib/python3.5/dist-packages/'])
            result = subprocess.run(['cp',pwd+'/config/ansible.cfg','/etc/ansible/ansible.cfg'])
            result = subprocess.run(['cp',pwd+'/config/value_info',pwd+'/ansible/files/initial_value_setting/'])
            if (os.path.exists(pwd+'/interfaces') == False):
                result = subprocess.run(['mkdir',pwd+'/interfaces'])
        elif(input_result == "q"):
            exit(0)
    else:
        print("Ansible is here!!! no more ansible install.. just copy ansible.cfg to /etc/ansible/")
        result = subprocess.run(['cp',pwd+'/config/ansible.cfg','/etc/ansible/ansible.cfg'])
    result = subprocess.run(['cp',pwd+'/config/ansible.cfg','/etc/ansible/ansible.cfg'])

def install_ansible_apt():
    pwd=os.getcwd()
    result = subprocess.run(['apt-get','install','software-properties-common','-y'])
    result = subprocess.run(['apt-add-repository','ppa:ansible/ansible','-y'])
    result = subprocess.run(['apt-get','update'])
    result = subprocess.run(['apt-get','install','ansible','-y',])
    result = subprocess.run(['cp',pwd+'/config/ansible.cfg','/etc/ansible/ansible.cfg'])
    result = subprocess.run(['cp',pwd+'/config/value_info',pwd+'/ansible/files/initial_value_setting/'])
    if (os.path.exists(pwd+'/interfaces') == False):
        result = subprocess.run(['mkdir',pwd+'/interfaces'])

def retrive_ansible():
    result = subprocess.run(['sshpass','-p','tmax@cloud','scp','-r','root@175.195.163.11:~/automation/170331/',gvar.const.ANSIBLE_HOME],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)



