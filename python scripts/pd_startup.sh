#!/bin/bash
# this script will start Pd in no gui mode

sudo -H -u pi bash -c bash "echo 'starting Pd now'"
pd -nogui /home/pi/loppi/step-vibrato.pd &

/home/pi/loppi/lop2pd.py &
