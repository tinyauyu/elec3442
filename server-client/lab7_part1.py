import RPi.GPIO as GPIO
import time
import socket 
from raspirobotboard import *

import threading

GPIO.setmode(GPIO.BCM)
TRIG = 14
ECHO = 15

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG, False)

def getDistance(TRIG, ECHO):
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()     
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance

rr = RaspiRobot()

PORT = 12349

def ServerThread ():
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
            print("waiting command...")
            msg = con.recv(1024).decode().split(" ")
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
                dist = getDistance(TRIG, ECHO)
                print("distance: %s" % str(dist))
            else:
                print("Message: %s" % msg)        

server = threading.Thread(target=ServerThread, args=[])
server.start()
