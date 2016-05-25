from flask import Flask, render_template
import RPi.GPIO as GPIO
import time
import socket 
from raspirobotboard import *

from threading import Thread
import threading
import serial


rr = RaspiRobot()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('beauty.html')


@app.route('/up-move/')
def up_move():
    rr.forward()
    
 

@app.route('/left-move/')
def left_move():
    rr.right()


@app.route('/right-move/')
def right_move():
    rr.left()


@app.route('/down-move/')
def down_move():
    rr.reverse()


@app.route('/stop-move/')
def stop_move():
    rr.stop()
    return render_template('client.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='1232')
