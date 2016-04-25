import time
import RPi.GPIO as gpio

buzzer = 21

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
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