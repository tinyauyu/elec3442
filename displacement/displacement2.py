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

iteration = 10

lasttime = current_milli_time()

for i in range(1, iteration):
        _x, _y, _z = sense.get_accelerometer_raw().values()
        x = x + _x
        y = y + _y
        z = z + _z
    
    init_x=round(x*1.0 / iteration, 3)
    init_y=round(y*1.0 / iteration, 3)
    init_z=round(z*1.0 / iteration, 3)

init_x = round(init_x, 3)
init_y = round(init_y, 3)
init_z = round(init_z, 3)

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
    x = 0
    y = 0
    z = 0

    currtime = current_milli_time()
    for i in range(1, iteration):
        _x, _y, _z = sense.get_accelerometer_raw().values()
        x = x + _x
        y = y + _y
        z = z + _z
    
    x=round(x*1.0 / iteration, 3)
    y=round(y*1.0 / iteration, 3)
    z=round(z*1.0 / iteration, 3)

    print("x=%s, y=%s, z=%s" % (x - init_x, y-init_y, z-init_z))

    # f_x = alpha*f_x + (1-alpha)*x
    # f_y = alpha*f_y + (1-alpha)*y
    # f_z = alpha*f_z + (1-alpha)*z

    # f_x=round(f_x, 3)
    # f_y=round(f_y, 3)
    # f_z=round(f_z, 3)

    # # print("x=%s, y=%s, z=%s" % (f_x - init_x, f_y - init_y, f_z - init_z))

    # dx = f_x-init_x
    # dy = f_y-init_y
    # dz = f_z-init_z

    # dtime = (currtime-lasttime)/1000.0

    # vx = dx * dtime
    # vy = dy * dtime
    # vz = dz * dtime

    # f_vx = alpha*f_vx + (1-alpha)*vx
    # f_vy = alpha*f_vy + (1-alpha)*vy
    # f_vz = alpha*f_vz + (1-alpha)*vz

    # # print("vx=%s, vy=%s, vz=%s" % (f_vx, f_vy, f_vz))

    # dx = dx + f_vx*dtime
    # dy = dy + f_vy*dtime
    # dz = dz + f_vz*dtime

    # dx=round(dx, 3)
    # dy=round(dy, 3)
    # dz=round(dz, 3)

    # print("dx=%s, dy=%s, dz=%s" % (dx, dy, dz))    

    # lasttime = currtime
