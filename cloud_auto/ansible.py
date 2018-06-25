import subprocess
import os
import shutil
import sys
from glob import glob
import paramiko
import host
sys.path.insert(0,'config/')
import gvar
import copy

class ansibleHost:
    def __init__(self, host_name, host_class, ipaddr):
        self.host_name = host_name
        self.host_class = host_class
        self.ipaddr = ipaddr



def ansible_cfg():
    #to do: In case of modify the basic config option
    try:
        shutil.copyfile(gvar.const.ANSIBLE_CUSTOM_CONFIG_PATH, gvar.const.ANSIBLE_CONFIG_PATH)
    except Exception as e:
        print(type(e).__name__)

def ansible_init():
    with open(gvar.const.ANSIBLE_HOME + 'hosts','r') as f:
        data = f.readlines()

        current_class = ''
        class_ip_list = []
        for line in data:
            line = line.replace('\r','')
            line = line.replace('\n','')
            line.strip()

            if line == '[ansible_main]':#target class
                current_class = line
                continue
            elif line == "":
                continue

            if '[ansible_main]' == current_class:
                class_ip_list.append(line)

        #ssh key gen and send to target host
        
    result = subprocess.run([gvar.const.ANSIBLE_HOME + '/new_run.sh','-H','localhost','proxyinit'])

def playbook(host_list, book_name):
    #build host informatino for ansible

    #copy ansible configuration file
    #ansible_cfg()

    book_list  = [ file_path for dp, dn, filenames in os.walk("./ansible/books") for file_path in glob(os.path.join(dp,'*.yml'))]
    book_name = book_name + ".yml"
    is_success = False
    for book_file in book_list:
        if os.path.isfile(book_file) == False:
            continue
        if os.path.basename(book_file) == book_name:
#            result = subprocess.run(['ansible-playbook', book_file,"-e", "hosts=$" + host_list, "-v"] , stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#            print(result)
            p = subprocess.Popen(['ansible-playbook', book_file,"-e", "hosts=" + host_list, "-v"] , stdout=subprocess.PIPE)
            while p.poll() is None:
                l = p.stdout.readline()
                print(l.decode('utf-8'),end="")
#                print(str(l.strip(),'utf-8'))
#            print(str(p.stdout.read(),'utf-8'))
            is_success = True
            break
    if is_success == False:
        print("No such book file (./book)")

def build_ansible_hosts():
    host_list = host.InfoList(gvar.const.SYSTEM_HOST_FILE)
    
    ansible_host_list = []
    for host_info in host_list.HostInfo_list:
        for iface_info in host_info.ifaceInfo_list:
            if iface_info.management != "":
                ansible_host = ansibleHost(
                    host_info.host_name,
                    host_info.host_class,
                    iface_info.ipv4)
                ansible_host_list.append(copy.copy(ansible_host))

    x = sorted( ansible_host_list , key=lambda ansibleHost:ansibleHost.host_class )

    with open(gvar.const.ANSIBLE_HOST_FILE,'w') as f:
        current_class = ""
        for ansible_host in x:
            if current_class != ansible_host.host_class:
                current_class = ansible_host.host_class
                f.write("["+current_class+":children]\n")          
            f.write(ansible_host.host_name+"\n")
        
        f.write("\n\n")

        for ansible_host in x:
            f.write("["+ansible_host.host_name+"]\n"+ansible_host.ipaddr+"\t\t"+"ansible_user="+gvar.const.ANSIBLE_USER_ID+"\n")

#to do :  post verification process, known_host problem 
def ssh_root_establish(host, 
    user_name = gvar.const.ANSIBLE_USER_ID, user_pass = gvar.const.ANSIBLE_USER_PW, 
    root_name = gvar.const.ANSIBLE_ROOT_ID, root_pass = gvar.const.ANSIBLE_ROOT_PW):

    #as user permission
    #get establish status
    already_established_host = False
#    try:
#        ssh = paramiko.SSHClient()
#        ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
#        ssh.connect( host , username = root_name, password = root_pass)
#        already_established_host = True
#
#    except Exception as e:
#        print(type(e).__name__)
#        print("Fail to connect to " + host)
#
#    finally:
#        ssh.close()

    if(already_established_host == False):
        public_key = ""
        with open(gvar.const.SSH_PUBKEY_PATH,'r') as k: #cat >>
            public_key = k.readline()
        public_key = public_key.strip('\n')
    
        echo_command = public_key + " >> /root/.ssh/authorized_keys"
        sed_command = "sed -i s/PermitRootLogin\ prohibit-password/PermitRootLogin\ yes/ /etc/ssh/sshd_config"

        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
            ssh.connect( host , username = user_name, password = user_pass)
            #mkdir .ssh dir if dir is already exist, command will be skipped by bash with msg
            stdin, stdout, stderr = ssh.exec_command("mkdir /root/.ssh")
            #copy ssh pub key to remote
            stdin, stdout, stderr = ssh.exec_command("sudo -S bash -c \"echo " + echo_command + "\"")
            stdin.write(root_pass + '\n')
            stdin.flush()

            # #root pw setting
            # stdin, stdout, stderr = ssh.exec_command("sudo -S passwd " + root_name)
            # stdin.write(root_pass + '\n')
            # stdin.flush()

            # stdin.write(root_pass + '\n')
            # stdin.flush()

            # stdin.write(root_pass + '\n')
            # stdin.flush()

            # #sshd config change
            # stdin, stdout, stderr = ssh.exec_command("sudo -S " + sed_command )
            # stdin.write(root_pass + '\n')
            # stdin.flush()

            # #sshd reboot
            # stdin, stdout, stderr = ssh.exec_command("sudo -S service sshd restart")
            # stdin.write(root_pass + '\n')
            # stdin.flush()

        except Exception as e:
            print(type(e).__name__)
            return False
        finally:
            ssh.close()
    return True
