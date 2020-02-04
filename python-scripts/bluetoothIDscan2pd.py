#!/usr/bin/python3
# install Bluez Python module
# sudo apt-get install python-bluez

import os
import time
import bluetooth

# my python script that communications with Pd

def send2Pd(message=''):
    # Send a message to Pd
    os.system("echo '" + message + "' | pdsend 3000 localhost udp")

while True:
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print("found %d devices" % len(nearby_devices))

    for addr, name in nearby_devices:
        print("  %s - %s" % (addr, name))
        message = '9 ' + addr # make a string for use with Pdsend
        send2Pd(message)
    time.sleep(10)
