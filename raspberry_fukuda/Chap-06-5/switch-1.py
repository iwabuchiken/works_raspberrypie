#!  /usr/bin/env python

# -*- coding: utf-8 -*-

############################
# setup: GPIOswitch-1.py
## 2016.09.26
############################
import RPi.GPIO as GPIO
import time

############################
# setup: GPIO
############################
GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)

############################
# on off
############################
while True:

    print( GPIO.input(9))

##    print("continuing...")

    GPIO.output(4, GPIO.HIGH)

    time.sleep(0.5)

    GPIO.output(4, GPIO.LOW)
    time.sleep(0.5)


############################
# closing
############################
GPIO.cleanup()
