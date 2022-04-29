Authors: Amar Barucija, Sean Richens, Daniel Toone
Class: CS6490 - Network Security
Final Project: Bluetooth DoS Attacks
----------------------------------------------------------------------------
Note: All following Python files are associated with this 
team’s final project. Each file is necessary for attempting
the approaches/attacks mentioned in this repository’s 
associated report. In no way should this files in this 
repository be used to to conduct any malicious attacks
against Bluetooth devices. Everything in this repository
is intended for educational purposes only.
The link for the associated final report is below…

https://docs.google.com/document/d/1cEFSq8iwElDhSbyVv0iVbbAzbaGqRiPyKoLz35p2PiM/edit?usp=sharing

----------------------------------------------------------------------------
btClient.py, btServerSecure.py, btServerVulnerable.py

btServerSecure.py, btServerVulnerable.py, and btClient.py are used to create simulated bluetooth devices to test DoS attacks on.

The job of btClient is to send timestamps to btServer so that it is able to determine how long it has been since the client has sent the packet. This is used to see if the dos attack has any effect on the server.

The secure version of the server implements a mitigation to stop the spamming of connection requests by not accepting new connections if there is already a connection from the same MAC address.

Used in Scenario 1 - Approaches 1, 2, & 3



----------------------------------------------------------------------------
dosConnections.py

This Python program works by spamming Bluetooth connection requests to a specified MAC address. Multithreading is implemented into its code to allow for 100 individual threads to spam connection requests to a victim device. The connection requests are implemented by using a socket and specifying Bluetooth communication protocols on said socket. This program is designed and intended to run as long as the user would like it to run. 

Used in Scenario 1 - Approaches 2 & 3
Used in Scenario 2 - Approaches 1 & 2



----------------------------------------------------------------------------
dosPackets.py

This Python program works by spamming messages over Bluetooth communication to a specified MAC address. Each message consists of 1024 bytes where each byte is randomly generated. This program utilises a socket with Bluetooth communication protocols to be able to connect to a socket of a host or victim program containing the same protocols. This program works under the assumption that it can connect to the victim socket before being capable of attempting its attack.

Used in Scenario 1 - Approach 1



----------------------------------------------------------------------------
dosPingThreading.py

This Python program works by spamming Bluetooth pings to a specified MAC address. Multithreading is implemented to allow for 100 individual threads to spam Bluetooth pings to a victim device. The Bluetooth pings are run by the Linux command, l2ping. Therefore, this Python program can only be executed on a Linux device with a working Bluetooth module. This program is designed to spam tons of ping commands to hopefully stop or break bluetooth connections.

Used in Scenario 2 - Approach 3



----------------------------------------------------------------------------
dosPing.py

This Python program works by spamming Bluetooth pings to a specified MAC address. The Bluetooth pings are run by the Linux command, l2ping. Therefore, this Python program can only be executed on a Linux device with a working Bluetooth module. This program is designed to continually send ping commands to a bluetooth device to stop another from connecting to it.

Used in Scenario 2 - Approach 4
