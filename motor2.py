import RPi.GPIO as gpio
import time


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





