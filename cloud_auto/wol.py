import socket, struct
import utils


class EtherWaker():

    def validateMacChk(self, mac_address):
        #to do : write mac address chk regx 
        if len(mac_address) == 12:
            self.mac_address = mac_address
        elif len(mac_address) == 17:
            delimeter = mac_address[2]
            self.mac_address = mac_address.replace(delimeter, '')
        else:
            raise ValueError('Incorrect Mac Address')   
        
    def buildMagicPacket(self):
        self.magic_packet = b'xFF' * 6 + self.mac_address * 16


    def sendPacket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(self.mac_address, ('', 9))
        sock.close()

    def wakeOnLan(self, mac_address):
        self.validateMacChk(mac_address)
        self.buildMagicPacket()
        self.sendPacket()
