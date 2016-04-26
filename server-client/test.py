import time
import socket 

import threading

PORT = 12346

def Server1Thread ():
    while(True):
    	print("test1")

        
def Server2Thread ():
    while(True):
    	print("test2")


server = threading.Thread(target=Server1Thread, args=[])
server.start()
server2 = threading.Thread(target=Server2Thread, args=[])
server2.start()