import RPi.GPIO as GPIO
import time

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

print "Waiting For Sensor To Settle"

time.sleep(2)
distance = getDistance(TRIG, ECHO)
print "Distance:",distance,"cm"

GPIO.cleanup()
