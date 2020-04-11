#Tool for Scanning port


import sys
from datetime import datetime
import socket


if (len(sys.argv))==2:
    target=socket.gethostbyname(sys.argv[1])
else:
    print("Incorrect Syntax / Number of arguments")
    print("Syntax: python3 portscanner.py <ip> ")

print("PORT SCANNER IS SCANNING ")
print(datetime.now())


try:
    for port in range(40,81):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result=s.connect_ex((target,port))
        print(port)
        if result==0:
            print("The %d is open"%(port))
        s.close()

except KeyboardInterrupt:
    print("Exiting script")
    sys.exit()
except socket.gaierror:
    print("Host Name Could not be Resolved")
    sys.exit()
except socket.error:
    print("Couldnt connect to server")
    sys.exit()