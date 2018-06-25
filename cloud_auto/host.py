import copy, utils

IFACE_INFO_ATTR_LIST = [
    'iface_name',
    'vlan_raw_dev',
    'ipv4',
    'ipv6',
    'netmask',
    'gateway',
    'dns',
    'pseudomac',
    'hwmac',
    'switch_port',
    'switch_dpid',
    'management'#for ansible
]
class IfaceInfo:
    def __init__(self, iface_name="", ipv4="", ipv6="",pseudomac="", dns="" , hwmac="" ):
        self.iface_name = iface_name
        self.vlan_raw_dev = ""
        self.ipv4 = ipv4
        self.ipv6 = ipv6
        self.netmask = ""
        self.gateway = ""
        self.dns = dns
        self.pseudomac = pseudomac
        self.hwmac = hwmac
        self.switch_port = ""
        self.switch_dpid = ""
        self.management = ""


HOST_INFO_ATTR_LIST = [
    'host_name',
    'host_class',
    'tag'
]
class HostInfo:
    def __init__(self, host_name="", host_class="", tag=""):
        self.host_name = host_name
        self.host_class = host_class
        self.tag = tag
        self.ifaceInfo_list = []

    def get_iface(self, iface_name):
        for iface_info in self.ifaceInfo_list:
            if iface_info.iface_name == iface_name:
                return iface_info
        
        raise ValueError('No such interface name in Host Information. Check ./config/host_info')  

class InfoList:
    def __init__(self, host_info_path="", info_list = []):
        if host_info_path != "":
            self.parse_info(host_info_path)
        elif info_list != []:
            self.HostInfo_list = info_list
    
    def parse_info(self,host_info_path):
        with open(host_info_path,'r') as f:
            data = f.readlines()

        self.HostInfo_list = []

        rHostInfo = None
        rIfaceInfo = None

        for line in data:
            line = line.strip()
            if line == '':
                continue
            
            if '#' in line:
                continue

            try:
                key = line.split(':' , 1)[0]
                value = line.split(':' , 1)[1]
            except Exception as e:
                print(e)
                continue
            else:
                key = key.strip()
                value = value.strip()

            if key == 'host':
                if rIfaceInfo != None:
                    rHostInfo.ifaceInfo_list.append(copy.copy(rIfaceInfo))
                    del rIfaceInfo
                    rIfaceInfo = None
                if rHostInfo != None:
                    self.HostInfo_list.append(copy.copy(rHostInfo))
                    del rHostInfo
                rHostInfo = HostInfo()
            elif key == 'interface':
                pass
            elif key == 'iface':
                if rIfaceInfo != None:
                    rHostInfo.ifaceInfo_list.append(copy.copy(rIfaceInfo))
                    del rIfaceInfo
                rIfaceInfo = IfaceInfo()
                rIfaceInfo.management = value
            elif key == 'host_name':
                rHostInfo.host_name = value
            elif key == 'host_class':
                rHostInfo.host_class = value
            elif key == 'tag':
                rHostInfo.tag = value
            elif key == 'iface_name':
                rIfaceInfo.iface_name = value
            elif key == 'vlan_raw_dev':
                rIfaceInfo.vlan_raw_dev = value
            elif key == 'ipv4':
                if utils.chk_valid_ipv4(value):
                    rIfaceInfo.ipv4 = value
                #else:
                #    print("invalid IPv4 Addr")
            elif key == 'ipv6':
                rIfaceInfo.ipv6 = value
            elif key == 'netmask':
                rIfaceInfo.netmask = value
            elif key == 'gateway':
                rIfaceInfo.gateway = value
            elif key == 'dns':
                rIfaceInfo.dns = value
            elif key == 'pseudomac':
                if utils.chk_valid_mac(value):
                    rIfaceInfo.pseudomac = value
                else:
                    print("Invalid mac address")
            elif key == 'hwmac':
                if utils.chk_valid_mac(value):
                    rIfaceInfo.hwmac = value
                else:
                    print("Invalid mac address")
            elif key == 'switch_port':
                rIfaceInfo.switch_port = value
            elif key == 'switch_dpid':
                rIfaceInfo.switch_dpid = value
        
        if rIfaceInfo.iface_name != '':
            rHostInfo.ifaceInfo_list.append(copy.copy(rIfaceInfo))

        self.HostInfo_list.append(copy.copy(rHostInfo))

    def write_info(self):
        with open("./host_info_test",'w') as f:
            for host_info in self.HostInfo_list:
                f.write("host:\n")
                f.write("  " + HOST_INFO_ATTR_LIST[0] + ":" + host_info.host_name + "\n")
                f.write("  " + HOST_INFO_ATTR_LIST[1] + ":" + host_info.host_class + "\n")
                f.write("  " + HOST_INFO_ATTR_LIST[2] + ":" + host_info.tag + "\n")
                f.write("iface:" + "\n")
                for iface_info in host_info.ifaceInfo_list:
                    if iface_info.management == "":
                        f.write("    if:" + "\n")
                    else:
                        f.write("    if:*" + "\n")

                    if iface_info.iface_name != "":
                        f.write("      " + IFACE_INFO_ATTR_LIST[0] + ":" + iface_info.iface_name + "\n")
                    if iface_info.vlan_raw_dev != "":
                        f.write("      " + IFACE_INFO_ATTR_LIST[1] + ":" + iface_info.vlan_raw_dev + "\n")
                    if iface_info.ipv4 != "":
                        f.write("      " + IFACE_INFO_ATTR_LIST[2] + ":" + iface_info.ipv4 + "\n")
                    if iface_info.ipv6 != "":
                        f.write("      " + IFACE_INFO_ATTR_LIST[3] + ":" + iface_info.ipv6 + "\n")
                    if iface_info.netmask != "":
                        f.write("      " + IFACE_INFO_ATTR_LIST[4] + ":" + iface_info.netmask + "\n")
                    if iface_info.gateway != "":
                        f.write("      " + IFACE_INFO_ATTR_LIST[5] + ":" + iface_info.gateway + "\n")
                    if iface_info.dns != "":
                        f.write("      " + IFACE_INFO_ATTR_LIST[6] + ":" + iface_info.dns + "\n")
                    if iface_info.pseudomac != "":
                        f.write("      " + IFACE_INFO_ATTR_LIST[7] + ":" + iface_info.pseudomac + "\n")
                    if iface_info.hwmac != "":
                        f.write("      " + IFACE_INFO_ATTR_LIST[8] + ":" + iface_info.hwmac + "\n")
                    if iface_info.switch_port != "":
                        f.write("      " + IFACE_INFO_ATTR_LIST[9] + ":" + iface_info.switch_port + "\n")
                    if iface_info.switch_dpid != "":
                        f.write("      " + IFACE_INFO_ATTR_LIST[10] + ":" + iface_info.switch_dpid + "\n")                  

                f.write("\n")

                
        # with open("./host_info",'w') as f:
            # pass

    def get_host(self, host_name = "", host_class = "", tag = "" , exact_match=True):
        if host_name != "":
            for host_info in self.HostInfo_list:
                if host_info.host_name == host_name:
                    return host_info
            raise ValueError('No such host name in Host Information. Check ./config/host_info')

        elif host_class != "":
            rHostInfo_list = []
            for host_info in self.HostInfo_list:
                if host_info.host_class == host_class:
                    rHostInfo_list.append(host_info)

            if len(rHostInfo_list) == 0:
                raise ValueError('No such class name in Host Information. Check ./config/host_info')
            else:
                tmp_list = InfoList(rHostInfo_list)
                return tmp_list

        elif tag != "":
            rHostInfo_list = []
            for host_info in self.HostInfo_list:
                if host_info.tag == tag:
                    rHostInfo_list.append(host_info)

            if len(rHostInfo_list) == 0:
                raise ValueError('No such tag in Host Information. Check ./config/host_info')
            else:
                tmp_list = InfoList(rHostInfo_list)
                return tmp_list

if __name__ == "__main__":
    host_info_list = InfoList("./host_info")
    host_info = host_info_list.get_host(host_name="C1-1")
    if_ip = host_info.ifaceInfo_list[0]
    print(if_ip.ipv4)
