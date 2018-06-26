#!/usr/bin/python

import OSC # install pyOSC library

c = OSC.OSCClient()
c.connect(('127.0.0.1', 9002))
oscmsg = OSC.OSCMessage()

def send2Pd(message=''):
    oscmsg.append(message)
    c.send(oscmsg)

def message1():
    oscmsg.setAddress("/lop/pot1")
    message = '500'
    send2Pd(message)

def message2():
    oscmsg.setAddress("/lop/pot2")
    message = '900'
    send2Pd(message)

message1()
message2()
message1()
