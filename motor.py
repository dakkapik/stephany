import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.out)
gpio.setup(22, gpio.out)
gpio.setup(27, gpio.out)

gpio.output(17, false)

time.sleep(4)

gpio.output(22, true)
gpio.output(27, false)

gpio.output(17, true)

time.sleep(4)

gpio.output(27, true)
gpio.output(22, false)

time.sleep(4)

gpio.output(17, false)
