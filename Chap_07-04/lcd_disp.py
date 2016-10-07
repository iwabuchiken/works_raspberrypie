#!  /usr/bin/env python

# -*- coding: utf-8 -*-

############################
# lcd_disp.py
## 20161005_175359
############################

############################
# imports
############################
import time
import smbus
from acm1602 import acm1602

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
# display()
############################
def display():

    lcd = acm1602( 1, 0x50, 4 )
    lcd.move_home()
    lcd.set_cursol( 0 )
    lcd.set_blink( 0 )

    lcd.backlight(1)

    lcd.write( "Raspberry Pi" )

    lcd.move( 0x00, 0x01 )
##    lcd.write( time.strftime("%H:%M") )
    lcd.write( time.strftime("%H:%M:%S") )


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
# display
display()

while True:

    # display
    display()

    # sleep

    time.sleep(1)
##
##    # cds
##    cds()
##
##    # pressure
##    pressure()
    
