import socket
PORT = 12340

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

while True:
	temp = sense.get_temperature()
	temp = round(temp,2)
	humidity = sense.get_humidity()
	humidity = round(humidity, 2)
	pressure = sense.get_pressure()
	pressure = round(pressure, 2)

	t = "TEMP " + str(temp)
	s.send(t.encode())
	h = "HUMD " + str(humidity)
	s.send(h.encode())
	p = "PRES " + str(pressure)
	s.send(p.encode())
	time.sleep(5) 
