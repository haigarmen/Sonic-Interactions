#!/usr/bin/python

import socket
import time      # import time for the sleep function
import spidev    # import the spidev module
import RPi.GPIO as GPIO

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

IP="127.0.0.1"
PORT=9002
addr=(IP, PORT)
EOL=';\n'

waitTime = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send2Pd(message=''):
    # Send a message to Pd
    message = message+EOL
    sock.sendto(message.encode('utf-8'), addr)

def readadc(channel):
    if channel > 7 or channel < 0:
        return -1
    r = spi.xfer2([1, 8 + channel << 4, 0])
    v = ((r[1] & 3) << 8) + r[2]
    return v;

while True:
    input_right = GPIO.input(4)
    input_left = GPIO.input(17)
    input_down = GPIO.input(18)
    input_up = GPIO.input(27)

    values = [0]*8

    for i in range(8):
        values[i] = readadc(i)
#        message =  '/lop /pot'+str(i+1) + ' ' + str(values[i]) # make a string for use with Pdsend
        message =  '/lop/pot' + '/' + str(values[i]) # make a string for use with Pdsend
        send2Pd(message)
        print(message)
#    print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
    time.sleep(waitTime)
