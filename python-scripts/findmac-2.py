#!/usr/bin/python

import bluetooth
import time
import urllib2

print "In/Out Board"

while True:
    print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())

    result = bluetooth.lookup_name('XX:XX:XX:XX:XX:XX', timeout=5)
    if (result != None):
        print "Jeroen: in"
        urllib2.urlopen("http://192.168.178.XXX/api/app/com.internet/presence/home").read()
    else:
        print "Jeroen: out"
        urllib2.urlopen("http://192.168.178.XXX/api/app/com.internet/presence/away").read()
    print "Sleeping for 10"
    time.sleep(10)
