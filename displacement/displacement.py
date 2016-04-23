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

f_x, f_y, f_z = sense.get_accelerometer_raw().values()
f_x=round(x, 0)
f_y=round(y, 0)
f_z=round(z, 0)

alpha = 0.2

while True:
    x, y, z = sense.get_accelerometer_raw().values()

    x=round(x, 0)
    y=round(y, 0)
    z=round(z, 0)

    f_x = alpha*f_x + (1-alpha)*x
    f_y = alpha*f_y + (1-alpha)*y
    f_z = alpha*f_z + (1-alpha)*z

    print("x=%s, y=%s, z=%s" % (f_x, f_y, f_z))