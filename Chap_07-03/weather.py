#!  /usr/bin/env python

# -*- coding: utf-8 -*-

############################
# weather.py
## 20161005_152258
############################

############################
# imports
############################
import time
import smbus
import mpl1152a2

import Adafruit_ADS1x15

############################
# vars
############################
GAIN = 1
adc = Adafruit_ADS1x15.ADS1015()

i2c_channel = 1
i2c = smbus.SMBus(i2c_channel)

##dac = i2c.read_i2c_block_data(

########################################################
# funcs
########################################################

############################
# cds()
############################
def cds():

    volts = adc.read_adc(0, gain=GAIN) / 500.0
    
    if volts > 1:

        print( "Well lighted : " + str(volts) + " V" )

    else:

        print( "Dark : " + str(volts) + " V" )

############################
# pressure()
############################
def pressure():

    pres = mpl1152a2.getpressur(i2c_channel)

    print "Pressure : %.2f hPa" % pres
    
############################
# operations
############################
while True:

    cds()

    pressure()
    
##    volts = adc.read_adc(0, gain=GAIN) / 500.0
##    
##    if volts > 1:
##
##        print( "Well lighted : " + str(volts) + " V" )
##
##    else:
##
##        print( "Dark : " + str(volts) + " V" )

    time.sleep(1)
