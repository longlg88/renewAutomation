import os
import subprocess
import shutil
import sys
from glob import glob

sys.path.insert(0,'config/')
import gvar

def init_essential():
    result=subprocess.Popen(['sudo dpkg -l ansible'],shell=True, stdout=subprocess.PIPE)
    data=result.communicate()[0]
    if not data.decode('utf-8'):
        print("There is no ansible here")
    else:
        print("(1) uninstall ansible using apt-get (2) uninstall ansible using dpkg (q) quit")
        input_result=input()
        if(input_result == "1"):
            result = subprocess.run(['apt-get','purge','ansible','-y'])
        elif(input_result == "2"):
            result = subprocess.run(['sudo','dpkg','--purge','ansible'])
            result = subprocess.run(['sudo','dpkg','--purge','python-paramiko'])
            result = subprocess.run(['sudo','dpkg','--purge','python-cryptography'])
            result = subprocess.run(['sudo','dpkg','--purge','python-cffi-backend'])
            result = subprocess.run(['sudo','dpkg','--purge','python-ecdsa'])
            result = subprocess.run(['sudo','dpkg','--purge','python-enum34'])
            result = subprocess.run(['sudo','dpkg','--purge','python-httplib2'])
            result = subprocess.run(['sudo','dpkg','--purge','python-idna'])
            result = subprocess.run(['sudo','dpkg','--purge','python-jinja2'])
            result = subprocess.run(['sudo','dpkg','--purge','python-markupsafe'])
            result = subprocess.run(['sudo','dpkg','--purge','python-pyasn1'])
            result = subprocess.run(['sudo','dpkg','--purge','python-yaml'])
        elif(input_result == "q"):
            exit(0)
