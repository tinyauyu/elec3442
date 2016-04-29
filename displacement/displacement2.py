from math import sin, cos, radians
from sense_hat import SenseHat
sense = SenseHat()

import time
current_milli_time = lambda: int(round(time.time() * 1000))
while True:

    currtime = current_milli_time()
    
    _x, _y, _z = sense.get_accelerometer_raw().values()
    pitch, roll, yaw = sense.get_orientation().values()
    
    p = radians(pitch)
    r = radians(roll)
    y = radians(yaw)

    x = _x*cos(y)+_y*sin(y)+_x*cos(r)+_z*sin(r)
    y = _x*sin(y)+_y*cos(y)+_y*cos(p)+_z*sin(p)
    z = _x*sin(r)+_z*cos(r)+_y*sin(p)+_z*cos(p)

    print("x=%s, y=%s, z=%s" % (x, y, z))

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
