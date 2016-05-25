import time
import RPi.GPIO as gpio

buzzer = 18

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)
gpio.setup(buzzer,gpio.OUT)

try:
    while True:
        gpio.output(buzzer,0)
        time.sleep(.3)
        gpio.output(buzzer,1)
        time.sleep(.3)
except KeyboardInterrupt:
    gpio.cleanup()
    exit