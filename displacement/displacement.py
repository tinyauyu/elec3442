from sense_hat import SenseHat

sense = SenseHat()

init_pitch, init_roll, init_yaw = sense.get_orientation().values()

while True:
    pitch, roll, yaw = sense.get_orientation().values()
    print("pitch=%s, roll=%s, yaw=%s" % (pitch-init_pitch,yaw-init_yaw,roll-init_roll))