import socket 
from raspirobotboard import *

rr = RaspiRobot()

PORT = 12346
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("",PORT))
print("Server created.")
server.listen(1)

check = 1

while check == 1:
    

    con, addr = server.accept()
    print ("Connected to %s:%s" % (addr[0],addr[1]))

    data = con.recv(1024)
    print(data.decode())
    con.send("Greetings from the server." .encode())

    while True:
        msg = con.recv(1024).decode().split(" ")
	dist = rr.get_range_inch()
        '''
        if msg[0] == "KILL":
            print("Shut down server.")
            con.close()
            server.close()
            check = 0
            break
        elif msg[0] == "SHOW":
            print(" ".join(msg[1:]))
        elif msg[0] == "MOVE":
            sense.set_pixel(*map(int, msg[1:6]))
        elif msg[0] == "REPEAT":  
            con.send(msg[1].encode())
        elif msg[0] == "EXIT":
            con.close()
            break
        else:
            print("Message: %s" % msg)
        '''
        if msg[0] == "UP":
            rr.forward()
        elif msg[0] == "DOWN":
            rr.reverse()
        elif msg[0] == "LEFT":
            rr.right()
        elif msg[0] == "RIGHT":  
            rr.left()
        elif msg[0] == "STOP":
            rr.stop()
	elif msg[0] == "DIST":
	    dist = rr.get_range_inch()
	    print("distance: %s" % str(dist))
        else:
            print("Message: %s" % msg)
        










        


