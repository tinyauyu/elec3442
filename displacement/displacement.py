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

import time
current_milli_time = lambda: int(round(time.time() * 1000))

f_x, f_y, f_z = sense.get_accelerometer_raw().values()
lasttime = current_milli_time()

f_x=round(f_x, 2)
f_y=round(f_y, 2)
f_z=round(f_z, 2)

init_x = f_x
init_y = f_y
init_z = f_z

alpha = 0.2

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
    x, y, z = sense.get_accelerometer_raw().values()
    currtime = current_milli_time()

    x=round(x, 2)
    y=round(y, 2)
    z=round(z, 2)

    f_x = alpha*f_x + (1-alpha)*x
    f_y = alpha*f_y + (1-alpha)*y
    f_z = alpha*f_z + (1-alpha)*z

    f_x=round(f_x, 2)
    f_y=round(f_y, 2)
    f_z=round(f_z, 2)

    # print("x=%s, y=%s, z=%s" % (f_x - init_x, f_y - init_y, f_z - init_z))

    dx = f_x-init_x
    dy = f_y-init_y
    dz = f_z-init_z

    dtime = (currtime-lasttime)/1000.0

    vx = dx * dtime
    vy = dy * dtime
    vz = dz * dtime

    f_vx = alpha*f_vx + (1-alpha)*vx
    f_vy = alpha*f_vy + (1-alpha)*vy
    f_vz = alpha*f_vz + (1-alpha)*vz

    print("x=%s, y=%s, z=%s" % (f_vx, f_vy, f_vz))

    dx = dx + f_vx*dtime
    dy = dy + f_vy*dtime
    dz = dz + f_vz*dtime

    print("x=%s, y=%s, z=%s" % (dx, dy, dz))    

    lasttime = currtime
