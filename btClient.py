import socket
from datetime import datetime
import time
import struct

#Mac address removed for privacy and security reasons
serverMACAddress = ''
port = 4

#Connects to the server
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))

#Continually sends timestamps to the server every second 
while 1:
    time.sleep(1)
    timestamp = time.time()
    print(timestamp)
    s.send(struct.pack('d',timestamp))
s.close()