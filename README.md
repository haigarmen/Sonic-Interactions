<h2>Loppi</h2>
Loppi is a new musical instrument using Raspberry Pi with Lots of Pots Shield (https://moderndevice.com/product/lots-of-pots-lop-board-for-raspberry-pi/).

Using Python to read the potentiometers and send data to Pure Data (https://puredata.info/) to generate sequences and audio. The current communication protocol is SpiDev but I may try pyOSC to compare performance.

<h3>Installing Software</h3>
To install PureData on a Raspberry Pi type the following into the terminal window:
<pre>
sudo apt-get install puredata
</pre>

<h3>Installing Externals for PureData</h3>
The Vanilla version of PureData can be extended with libraries called Externals, which can be found under the help menu in Find Externals.

<h3>References</h3>
http://www.instructables.com/id/Pure-Pi-Control-custom-stompbox-effects-on-a-Raspb/

http://www.instructables.com/id/PiMiDi-A-Raspberry-Pi-Midi-Box-or-How-I-Learned-to/

https://guitarextended.wordpress.com/2011/12/12/installing-pure-data/
