from sense_hat import SenseHat

sense = SenseHat()

##### Angle detection

# init_pitch, init_roll, init_yaw = sense.get_orientation().values()

# while True:
#     pitch, roll, yaw = sense.get_orientation().values()
#     print("pitch=%s, roll=%s, yaw=%s" % (pitch-init_pitch,yaw-init_yaw,roll-init_roll))


##### Displacement detection
from sense_hat import SenseHat

sense = SenseHat()

while True:
    x, y, z = sense.get_accelerometer_raw().values()

    x=round(x, 0)
    y=round(y, 0)
    z=round(z, 0)

    print("x=%s, y=%s, z=%s" % (x, y, z))