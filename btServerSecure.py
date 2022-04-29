import socket
from datetime import datetime
import time
import struct
import threading

#Mac address removed for privacy and security reasons
hostMACAddress = ''
port = 4

backlog = 1
size = 1024
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((hostMACAddress,port))
s.listen(backlog)

#The client that will run on a seperate thread
def client(clientsocket, address):
    try:
        while 1:
            data = clientsocket.recv(size)

            #If there is data parse it as a timestamp to see how long it took to receive.
            #Used to see if a DoS attack is causing any problems 
            if data:
                recievedtimestamp = struct.unpack('d',data)[0]
                timestamp = time.time()
                difftime = timestamp - recievedtimestamp
                print(difftime)

    except:	
        print("Closing socket")	
        client.close()
        s.close()

connections = [] #keeps track of the already connected clients

#Continually accepts new clients 
while True:
    clientsocket, address = s.accept()

    #If the address has already been made don't allocate recources and close the newly created connection
    if address[0] in connections:
        clientsocket.close()
    else:
        connections.append(address[0])
        print("made a connection")
        clientThread = threading.Thread(target=client, args=(clientsocket,address,))
        clientThread.start()
        
