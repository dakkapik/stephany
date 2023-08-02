import RPi.GPIO as gpio
import time


gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT)
gpio.setup(22, gpio.OUT)
gpio.setup(27, gpio.OUT)

def forward():
    gpio.out(22,True )
    gpio.out(27, False)

def backward():
    gpio.out(22, False)
    gpio.out(27, True)

def turnOn():
    gpio.out(17,True)

def turnOff():
    gpio.out(17, False)

turnOn()
forward()
time.sleep(5)
backward()
time.sleep(5)
turnOff()





