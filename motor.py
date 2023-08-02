import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT)
gpio.setup(22, gpio.OUT)
gpio.setup(27, gpio.OUT)

gpio.output(17, False)

time.sleep(4)

gpio.output(22, True)
gpio.output(27, False)

gpio.output(17, True)

time.sleep(4)

gpio.output(27, True)
gpio.output(22, False)

time.sleep(4)

gpio.output(17, False)