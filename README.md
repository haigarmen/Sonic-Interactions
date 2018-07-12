# Sonic Interactions
Sonic Interactions is a research project (http://sonicinteractions.org) exploring what happens when people interact with technology to create music. For centuries we have carefully handcrafted the interactions of musical instruments, optimizing them for comfort, intuitive learning, and playability yet many of the newest tools of musical expression are cold, intangible and use technologies in ways that ignore hundreds of years of accumulated knowledge. This research aims to bridge cognitive and social science with computational and humanistic approaches to create more expressive musical experiences and to expand the practice of Interaction Design. This research begins with a series of hands-on workshops in 2018.

## Sonic Interactions Workshop
The Sonic Interactions workshops aims to expand our creative repertoire by introducing basic electronics and coding in the context of musical instruments to explore a variety of tangible ways for us to interact with sound to create music. Using design sprints and accessible prototyping tools like Raspberry Pi and sensors, we aim to combine emergent technologies with existing instruments to create new instruments optimized for musical expression and interactivity. This code repo is initially created to share the code used for the workshop, including the code used to create the Sonic Interactions Pi Kit.

### Workshop Goals:



## Sonic Interactions Pi Kit
It was important to us to create an accessible open source audio kit for the workshops. We chose to use the popular Raspberry Pi with the following add-ons:
1. Lots of Pots expansion board
(https://moderndevice.com/product/lots-of-pots-lop-board-for-raspberry-pi/)

2. USB Audio Adapter
The Pi comes with sound but only a low quality output, this [adapter](https://www.adafruit.com/product/1475) adds higher quality input and output.

Using Python to read the potentiometers and send data to Pure Data (https://puredata.info/) to generate sequences and audio. The current communication protocol is SpiDev but I may try pyOSC to compare performance.

![Lots of Pots Board](http://sonicinteraction.design/wp-content/uploads/2018/07/lop3.jpg)

### Installing Software
To install PureData on a Raspberry Pi type the following into the terminal window:
<pre>
sudo apt-get install puredata
</pre>

### Installing Externals for PureData
The Vanilla version of PureData can be extended with libraries called Externals, which can be found under the help menu in Find Externals

### How the Software Stack in SIP Kit Works
![SIP Kit System Diagram](http://sonicinteraction.design/wp-content/uploads/2018/07/system-diagram.png)

Feedback from Workshop ECU (18.07.09)
- preworkshop email with details about what is needed
- integrating theory, making,
