#!/usr/bin/python

import os        # import os for sending messages to PD
import spidev    # import the spidev module
import time      # import time for the sleep function
import RPi.GPIO as GPIO

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

waitTime = .1
bounceTime = 0.1

btn1alreadyPressed = False
btn2alreadyPressed = False
btn3alreadyPressed = False
btn4alreadyPressed = False

GPIO.setmode(GPIO.BCM)
## GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4, GPIO.IN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(27, GPIO.IN)
 
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
    r = spi.xfer2([1, 8 + channel << 4, 0])

    # Three bytes are returned; the data (0-1023) is in the
    # lower 3 bits of byte 2, and byte 3 (datasheet figure 6-1)
    v = ((r[1] & 3) << 8) + r[2]

    return v;

while True:
    btn1pressed = not GPIO.input(4)
    btn2pressed = not GPIO.input(17)
    btn3pressed = not GPIO.input(18)
    btn4pressed = not GPIO.input(27)

    input_right = GPIO.input(4)
    input_left = GPIO.input(17)
    input_down = GPIO.input(18)
    input_up = GPIO.input(27)

    if btn1pressed and not btn1alreadyPressed:
        message = '8 1'
        send2Pd(message)
    btn1alreadyPressed = btn1pressed

    if btn2pressed and not btn2alreadyPressed:
 #       print('2 Pressed')
        message = '8 2'
        send2Pd(message)
    btn2alreadyPressed = btn2pressed

    if btn3pressed and not btn3alreadyPressed:
 #       print('3 Pressed')
        message = '8 3'
        send2Pd(message)
    btn3alreadyPressed = btn3pressed

    if btn4pressed and not btn4alreadyPressed:
 #       print('4 Pressed')
        message = '8 4'
        send2Pd(message)
    btn4alreadyPressed = btn4pressed

    values = [0]*8
    
    for i in range(8):
        values[i] = readadc(i)
        message = str(i) + ' ' + str(values[i]) # make a string for use with Pdsend
        send2Pd(message)

# consider creating a message that has all values in one string rather than separate messages
#    print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
#    print(message)
    time.sleep(waitTime)