PORT = 12300

import socket
import time

from sense_hat import SenseHat
sense = SenseHat()
sense.clear()
# while True:
# 	temp = sense.get_temperature()
# 	temp = round(temp,2)
# 	humidity = sense.get_humidity()
# 	humidity = round(humidity, 2)
# 	pressure = sense.get_pressure()
# 	pressure = round(pressure, 2)
# 	print("temperature: %s, humidity: %s, pressure: %s" % temp, humidity, pressure)

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
s.connect(('192.168.1.104', PORT))

s.send('hihi'.encode())
reply = s.recv(1024)

lastUpdate = time.time()

f_x, f_y, f_z = sense.get_accelerometer_raw().values()

f_x=round(f_x, 3)
f_y=round(f_y, 3)
f_z=round(f_z, 3)

init_x = f_x
init_y = f_y
init_z = f_z

alpha = 0.1

vx = 0
vy = 0
vz = 0

f_vx = vx
f_vy = vy
f_vz = vz

dx = 0
dy = 0
dz = 0

while True:
	currTime = time.time()
	if(currTime-lastUpdate>5):
		temp = sense.get_temperature()
		temp = round(temp,2)
		humidity = sense.get_humidity()
		humidity = round(humidity, 2)
		pressure = sense.get_pressure()
		pressure = round(pressure, 2)
		pitch, roll, yaw = sense.get_orientation().values()

		x, y, z = sense.get_accelerometer_raw().values()

	    x=round(x, 3)
	    y=round(y, 3)
	    z=round(z, 3)

	    f_x = alpha*f_x + (1-alpha)*x
	    f_y = alpha*f_y + (1-alpha)*y
	    f_z = alpha*f_z + (1-alpha)*z

	    f_x=round(f_x, 3)
	    f_y=round(f_y, 3)
	    f_z=round(f_z, 3)

	    # print("x=%s, y=%s, z=%s" % (f_x - init_x, f_y - init_y, f_z - init_z))

	    dx = f_x-init_x
	    dy = f_y-init_y
	    dz = f_z-init_z

	    dtime = (currTime-lastUpdate)

	    vx = dx * dtime
	    vy = dy * dtime
	    vz = dz * dtime

	    f_vx = alpha*f_vx + (1-alpha)*vx
	    f_vy = alpha*f_vy + (1-alpha)*vy
	    f_vz = alpha*f_vz + (1-alpha)*vz

	    # print("vx=%s, vy=%s, vz=%s" % (f_vx, f_vy, f_vz))

	    dx = dx + f_vx*dtime
	    dy = dy + f_vy*dtime
	    dz = dz + f_vz*dtime

	    dx=round(dx, 3)
	    dy=round(dy, 3)
	    dz=round(dz, 3)

	    # print("dx=%s, dy=%s, dz=%s" % (dx, dy, dz))

	    t = "ENVR " + str(temp) + " " + str(humidity) + " " + str(pressure) + " " + str(yaw - init_yaw) + " " + str(dx) + " " + str(dy) + " " + str(dz)
		s.send(t.encode())

		lastUpdate=currTime


