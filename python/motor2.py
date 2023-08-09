import RPi.GPIO as gpio
import time
import socketio

sio = socketio.Client()

gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT)
gpio.setup(22, gpio.OUT)
gpio.setup(27, gpio.OUT)

def forward():
    gpio.output(22,True )
    gpio.output(27, False)

def backward():
    gpio.output(22, False)
    gpio.output(27, True)

def turnOn():
    gpio.output(17,True)

def turnOff():
    gpio.output(17, False)

turnOn()
forward()
time.sleep(5)
backward()
time.sleep(5)
turnOff()

@sio.event
def connect():
    sio.emit("ID", 'steph-pi')
    print('connection established')
    turnOn()

@sio.event
def movePi(direction):
    print('recieved direction:  ', direction)
    if(direction == 'forward'):
        forward()
    else:
        backward()

@sio.event
def disconnect():
    print('disconnected from server')
    turnOn()

sio.connect('http://192.168.2.13:3000')
sio.wait()