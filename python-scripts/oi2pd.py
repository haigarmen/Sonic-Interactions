#!/usr/bin/python

import os        # import os for sending messages to PD
import spidev    # import the spidev module
import time      # import time for the sleep function
import RPi.GPIO as GPIO

# Open SPI bus
spi_1 = spidev.SpiDev()
spi_2 = spidev.SpiDev()

spi_1.open(0,0)
spi_2.open(0,1)

spi_1.max_speed_hz=1000000
spi_2.max_speed_hz=1000000

waitTime = .05
bounceTime = 0.1

btn1alreadyPressed = False
btn2alreadyPressed = False
btn3alreadyPressed = False
btn4alreadyPressed = False

GPIO.setmode(GPIO.BCM)
## GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN)
GPIO.setup(6, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(26, GPIO.IN)
GPIO.setup(6, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(19, GPIO.IN)

def send2Pd(message=''):
    # Send a message to Pd
    os.system("echo '" + message + "' | pdsend 3000 localhost udp")

def readadc(channel):
    if channel > 7 or channel < 0:
        return -1
    # spi.xfer2 sends three bytes and returns three bytes:
    # byte 1: the start bit (always 0x01)
    # byte 2: configure bits, see MCP3008 datasheet table 5-2
    # byte 3: don't care
    r = spi_1.xfer2([1, 8 + channel << 4, 0])
    # Three bytes are returned; the data (0-1023) is in the
    # lower 3 bits of byte 2, and byte 3 (datasheet figure 6-1)
    v = ((r[1] & 3) << 8) + r[2]

    return v;

def readadc2(channel):
    if channel > 7 or channel < 0:
        return -1
    # spi.xfer2 sends three bytes and returns three bytes:
    # byte 1: the start bit (always 0x01)
    # byte 2: configure bits, see MCP3008 datasheet table 5-2
    # byte 3: don't care
    r = spi_2.xfer2([1, 8 + channel << 4, 0])
    # Three bytes are returned; the data (0-1023) is in the
    # lower 3 bits of byte 2, and byte 3 (datasheet figure 6-1)
    v = ((r[1] & 3) << 8) + r[2]

    return v;

while True:
    btn1pressed = not GPIO.input(5)
    btn2pressed = not GPIO.input(6)
    btn3pressed = not GPIO.input(13)
    btn4pressed = not GPIO.input(19)

    if btn1pressed and not btn1alreadyPressed:
#        print('1 Pressed')
        message = '16 1'
        send2Pd(message)
    btn1alreadyPressed = btn1pressed

    if btn2pressed and not btn2alreadyPressed:
#        print('2 Pressed')
        message = '16 2'
        send2Pd(message)
    btn2alreadyPressed = btn2pressed

    if btn3pressed and not btn3alreadyPressed:
#        print('3 Pressed')
        message = '16 3'
        send2Pd(message)
    btn3alreadyPressed = btn3pressed

    if btn4pressed and not btn4alreadyPressed:
#        print('4 Pressed')
        message = '16 4'
        send2Pd(message)
    btn4alreadyPressed = btn4pressed
    
    values = [0]*8
    values2 = [0]*8
    
    for i in range(8):
        values[i] = readadc(i)
        values2[i] = readadc2(i)
        message = str(i) + ' ' + str(values[i]) # make a string for use with Pdsend
        message = message + ' ' + str(i+8) + ' ' + str(values2[i])
        send2Pd(message)

# consider creating a message that has all values in one string rather than separate messages
#    print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} '.format(*values) + '| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} '.format(*values2))
#    print(message)
    time.sleep(waitTime)