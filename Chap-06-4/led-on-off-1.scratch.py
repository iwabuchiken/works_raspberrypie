#!  /usr/bin/env python

# -*- coding: utf-8 -*-

##########################
# led-on-off-1.scratch.py
##########################


import RPi.GPIO as GPIO
import time

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.OUT)

############################
# on off
############################
while True:
    
    GPIO.output(4, GPIO.HIGH)
    time.sleep(1)

    GPIO.output(4, GPIO.LOW)
    time.sleep(1)
