# SPI_with_Adafruit_FT232H
USB to SPI connection using an Adafruit FT232H with Python


DESCRIPTION:
This code allows you to control SPI communication from your PC, using an Adafruit FT232H breakout board (https://www.adafruit.com/product/2264).
Your computer will be the Master, and determine the clock (SCKL) frequency.
This code is based on the following tutorials:
Tutorial No.1: https://learn.adafruit.com/circuitpython-on-any-computer-with-ft232h/overiew
Tutorial No.2: https://learn.adafruit.com/adafruit-ft232h-with-spi-and-i2c-libraries/spi-devices

HOW TO RUN:

1)
The first time, set up the drivers and libraries following Tutorial No.1:
    https://learn.adafruit.com/circuitpython-on-any-computer-with-ft232h/overiew
	
2)
If you're using Windows, make sure the FT232H appears in device manager (under libusbK USB devices), 
otherwise reinstall the driver from Zadig, as explained in Tutorial No.1:
	Open Zadig: select "options>list all devices"
	"USB serial converter" 
	Driver: "libusbK (v3.0.7.0)"
	Install Driver

3)
Adapt the code to yor needs.
Feel free to modify:
	-The CS pin that you prefer
	-The BAUD rate
	-The message sent

4) Connect SCLK, MISO and MOSI appropriately to your receiving slave device.
Connect CS from the pin you initialize in the code.
	
5)
From Windows, don't run script from your IDE. 
Open terminal or cmd line instead.
Run this line:
    set BLINKA_FT232H=1
And then this line:
    python SPIconnect.py
