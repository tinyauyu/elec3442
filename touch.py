import time
import RPi.GPIO as gpio

touch = 24

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(touch,gpio.IN)

try:
    while True:
        if(GPIO.input(touch)==1):
        	print("touched!")
        else:
        	print(".")
except KeyboardInterrupt:
    gpio.cleanup()
    exit