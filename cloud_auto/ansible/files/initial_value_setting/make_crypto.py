#!/usr/bin/python3
from Crypto.Cipher import AES
from cryptography.fernet import Fernet
import os
import sys
class pw_configure:
	
	def __init__(self):
		self.key=Fernet.generate_key()
		self.cipher_suite=Fernet(self.key)
		self.data_byte=bytearray()
		self.decoded_text=bytearray()
		self.encoded_text=bytearray()
	
	def encryption(self, data):
		self.data_byte=str.encode(data)
		self.encoded_text=self.cipher_suite.encrypt(self.data_byte)
		return self.encoded_text

	def decryption(self, data):
		self.decoded_text=self.cipher_suite.decrypt(data)
		return self.decoded_text

if __name__ == '__main__':
	'''
   obj = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')
   message = 'root!!23'
   ciphertext = obj.encrypt(message)
   print(ciphertext)
   obj2 = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')
   print(obj2.decrypt(ciphertext))
	key=Fernet.generate_key()
	cipher_suite=Fernet(key)
	'''
	try:
		c_auth=[]
		s_auth=[]
		m_auth=[]
		f=open("./value_info")
		lines=f.readlines()
		for x in range(len(lines)):
			if lines[x].startswith("#") == False:
				if 'C_accessAuth' in lines[x]:
					auth=input("input compute auth = ")
					c_auth.append(auth)

		print(c_auth)
	except KeyboardInterrupt:
		print("re execute program...")


#	obj = pw_configure()
#	print("encrypt = ",obj.encryption(data))
#	text=obj.encryption(data)
#	print("decrypt = ", obj.decryption(text))
