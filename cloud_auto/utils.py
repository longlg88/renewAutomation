import os, socket, re

def FileisExist(dirpath, tfilename):
    filenames = os.listdir(dirpath)
    for filename in filenames:
        if tfilename == filename:
            return True
    return False


def chk_valid_ipv4(addr):
    try:
        socket.inet_aton(addr)
        return True
    except socket.error as e:
        return False

def chk_valid_mac(addr):
    if re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", addr.lower()):
        return True
    else:
        return False

