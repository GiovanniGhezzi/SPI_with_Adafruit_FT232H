# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 14:35:30 2020

@author: John

Tutorial to run this code:
Make sure you followed this tutorial:
    https://learn.adafruit.com/circuitpython-on-any-computer-with-ft232h/overiew
Make sure the FT232H appears in device manager (under libusbK USB devices), 
otherwise install the driver from Zadig, as explained in tutorial.
(Zadig: options>list all devices, "USB serial converter" Driver: "libusbK (v3.0.7.0)", Install Driver)
Dont run script from IDE
Open terminal instead
Run this line:
    set BLINKA_FT232H=1
And then this line:
    python SPIconnect.py
"""
import time
import board
import busio
import digitalio

# import usb
#dev = usb.core.find(idVendor=0x0403, idProduct=0x6014)

# Create library object using our adafruit's SPI port
# create an interface to the SPI hardware bus:
# (i.e.: activate pins SCK, MOSI and MISO on the board)
spi = busio.SPI(board.SCK, board.MOSI, board.MISO) #SCK=D0, MOSI=D1, MISO=D2
# use pin C0 as CS output:
cs = digitalio.DigitalInOut(board.C0) #set pin C0 on the board as CS
cs.direction = digitalio.Direction.OUTPUT #direction: CLK is output (PC is master)

# CLK is high: in SPI protocol this means communication is off:
cs.value = True

spi.try_lock() # initiates communication
baudrate = 25000000 # MAX5144 freq = 25MHz
spi.configure(baudrate, phase=0, polarity=0) #configure values

# Communicate something:
cs.value = False #cs off = communication on
time.sleep(1) # 1 second delay
#while True: # While loop in case you need to transmit continuously
spi.write(bytes([0xD0, 0x00,])) # send bytes A1 and D0   
time.sleep(1) # 1 second delay
cs.value = True #cs on = communication off