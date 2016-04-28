import RPi.GPIO as GPIO
import time
import socket 
from raspirobotboard import *

from threading import Thread
import threading
import serial

###### Serial #####

last_received = ''
def receiving(ser):
    global last_received
    buffer = ''
    while True:
        buffer = buffer + ser.read(ser.inWaiting())
        if '\n' in buffer:
            lines = buffer.split('\n') # Guaranteed to have at least 2 entries
            last_received = lines[-2]
            #If the Arduino sends lots of empty lines, you'll lose the
            #last filled line, so you could make the above statement conditional
            #like so: if lines[-2]: last_received = lines[-2]
            buffer = lines[-1]


class SerialData(object):
    def __init__(self, init=50):
        try:
            self.ser = ser = serial.Serial(
                port='/dev/ttyUSB0',
                baudrate=9600,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                timeout=0.1,
                xonxoff=0,
                rtscts=0,
                interCharTimeout=None
            )
        except serial.serialutil.SerialException:
            #no serial connection
            self.ser = None
        else:
            Thread(target=receiving, args=(self.ser,)).start()
        
    def next(self):
        if not self.ser:
            return 100 #return anything so we can test when Arduino isn't connected
        #return a float value or try a few times until we get one
        for i in range(40):
            raw_line = last_received
            try:
                return float(raw_line.strip())
            except ValueError:
                return 'Noise'
                time.sleep(.005)
        return 0.
    def __del__(self):
        if self.ser:
            self.ser.close()


###################

PORT = 12347

GPIO.setmode(GPIO.BCM)
TRIG = 14
ECHO = 15
ALARM = 23
TOUCH = 24

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ALARM,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(TOUCH,GPIO.IN)
GPIO.output(TRIG, False)
GPIO.output(ALARM, False)

def getDistance(TRIG, ECHO):
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
        if(pulse_end - pulse_start > 5):
            print("Unable to get echo!")
            return -1
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance

rr = RaspiRobot()

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
            elif msg[0] == "TEMP":
                print("temperature: %s" % msg[1])
            elif msg[0] == "HUMD":  
                print("humidity: %s" % msg[1])
            elif msg[0] == "PRES":  
                print("pressure: %s" % msg[1])
            elif msg[0] == "EXIT":
                con.close()
                break
            elif msg[0] == "KILL":
                print("Shutdown server.")
                con.close()
                server.close()
                check=0
                break
            else:
                print("Message: %s" % msg)        

server = threading.Thread(target=ServerThread, args=[])
server.start()

def Alarm():
    for i in range(5):
        if GPIO.input(TOUCH)==1:
            return
        GPIO.output(ALARM, True)
        time.sleep(0.3)
        GPIO.output(ALARM, False)
        time.sleep(0.3)

def SerialGetThread():
    alarmThd = threading.Thread(target=Alarm, args=[])
    s = SerialData()
    isAlarm = False
    lastAlarm = time.time()
    while(True):
        in_str = s.next()
        print(in_str)
        if(type(in_str) is str) and (GPIO.input(TOUCH)==0):
            print ">>>>>>>>>>>>>> ALARM <<<<<<<<<<<<<<<<"
            try:
                alarmThd.start()
                lastAlarm = time.time()
            except:
                if alarmThd.isAlive() == False:
                    alarmThd = threading.Thread(target=Alarm, args=[])
        time.sleep(0.1)

serialThd = threading.Thread(target=SerialGetThread, args=[])
serialThd.start()

# def CollisionDetectionThread():
    
