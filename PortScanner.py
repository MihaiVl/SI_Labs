import socket
import subprocess
import sys
from threading import Thread

from datetime import datetime


remoteServer = input("Enter host name to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

print ("-" * 60)
print ("Please wait, scanning remote host", remoteServerIP)
print ("-" * 60)

t1 = datetime.now()
try:
    for port in range(1,150):
        t = Thread
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("Port {}: 	 Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print ("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print ('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print ("Couldn't connect to server")
    sys.exit()

t2 = datetime.now()

total =  t2 - t1

print ('Scanning Completed in: ', total)
