#!/usr/bin/env python3

import binascii
from Crypto.Cipher import AES

print("----------------")
print("This is a Key Value Checker for an AES key in UTF8 Input and uses ECB Mode")
print("AES key must be either 16, 24, or 32 bytes long")
print("----------------")

key = input("Please Enter AES KEY: ")
key = binascii.unhexlify(key)

aes = AES.new(key, AES.MODE_ECB)
data = "00000000000000000000000000000000"
data = binascii.unhexlify(data)

encd = aes.encrypt(data)

print("==========================================")
print("KCV: " + str(binascii.hexlify(encd))[1:])
print("KCV: " + str(binascii.hexlify(encd)[0:6])[1:])
