#Testing spamming packets of information to the simulated server to see if it effects the timestamp readings
#test: failed
import socket
import os
from time import sleep

#Mac address removed for privacy and security reasons
serverMACAddress = ''
port = 4 # needs to be even

s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))
#Continually sends random kilobyte of information to the server
while 1:
    s.send(os.urandom(1024))
s.close()