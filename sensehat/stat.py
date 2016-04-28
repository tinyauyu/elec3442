from sense_hat import SenseHat
sense = SenseHat()
sense.clear()
while True:
	temp = sense.get_temperature()
	temp = round(temp,2)
	humidity = sense.get_humidity()
	humidity = round(humidity, 2)
	pressure = sense.get_pressure()
	pressure = round(pressure, 2)
	print("temperature: %s, humidity: %s, pressure: %s" % temp, humidity, pressure)