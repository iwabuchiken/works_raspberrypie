#!  /usr/bin/env python

# -*- coding: utf-8 -*-

############################
# ADC-cds.py
## 20161005_131740
############################

###test
##import sys
##
##paths = sys.path
##
##for item in paths:
##
##    print item

############################
# imports
############################
import time, signal, sys

import Adafruit_ADS1x15

##import Adafruit_Python_ADS1x15
    ##Traceback (most recent call last):
    ##  File "analogin_cds.py", line 23, in <module>
    ##    import Adafruit_Python_ADS1x15
    ##ImportError: No module named Adafruit_Python_ADS1x15
##from Adafruit.ADS1x15 import Adafruit_ADS1x15
    ##Traceback (most recent call last):
    ##  File "analogin_cds.py", line 24, in <module>
    ##    from Adafruit.ADS1x15 import Adafruit_ADS1x15
    ##ImportError: No module named Adafruit.ADS1x15

############################
# vars
############################
GAIN = 1
##abc = Adafruit_ADS1015()
##adc = Adafruit_ADS1015()
adc = Adafruit_ADS1x15.ADS1015()

############################
# operations
############################
while True:

    volts = adc.read_adc(0, gain=GAIN) / 500.0
    
    if volts > 1:

        print( "Well lighted : " + str(volts) + " V" )

    else:

        print( "Dark : " + str(volts) + " V" )

    time.sleep(1)
