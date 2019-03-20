#!/usr/bin/python

import os        # import os for sending messages to PD
from nunchuck import nunchuck
import time

waitTime = .2

wii = nunchuck()
penstate = 0

def send2Pd(message=''):
    # Send a message to Pd
    os.system("echo '" + message + "' | pdsend 3000 localhost udp")


while True:
    if wii.button_c() == True:
        message = '16 1'
        send2Pd(message)
    if wii.button_z() == True:
        message = '17 1'
        send2Pd(message)
    # create an array with all the different data from nunchuck
    values = [0]*5
    values[0] = wii.joystick_y()
    values[1] = wii.joystick_x() 
    values[2] = wii.accelerometer_x()
    values[3] = wii.accelerometer_y()
    values[4] = wii.accelerometer_z()

    for i in range(5):
        message = str(i) + ' ' + str(values[i]) # make a string for use with Pdsend
        send2Pd(message)

#    print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} '.format(*values) + '| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} '.format(*values2))
#    print(values)
    time.sleep(waitTime)
