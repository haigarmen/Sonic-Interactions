# Sonic Interactions Research log

#### 17.11.08
# 1. Install PD on Pi #
- Pd doesn’t work on Newest Raspbian OS (stretch)
- Try on Jessie, Jessie lite is recommended (without gui)
- without gui can’t configure wifi without command line
update: Feb 2018 PD nows works on Raspbian Stretch

[https://guitarextended.wordpress.com/2013/01/28/rpi-as-guitar-effects-processor-installing-and-configuring-pd/](https://ccrma.stanford.edu/wiki/Lab1_Making_FX_in_Pd_2013)

[https://github.com/redFrik/raspberrypiWorkshop/blob/master/README.md](https://ccrma.stanford.edu/wiki/Lab1_Making_FX_in_Pd_2013)

controlling Pd from command line:
<code> pd -stderr -nogui -verbose testsines.pd</code>

#### 17.11.14:
Successful installed Pd on Raspbian Stretch.

#### 17.11.20
## how to get sensor data into PD?
## 1. Serial messages or 2. OSC
1. getting data from Sensor Hat in python
Communication with python
attempt 1: using socket - Pdsend
http://ccrma.stanford.edu/planetccrma/man/man1/pdsend.1.html
17.11.24 - got it working
17.11.26 sending joystick x value to Pd to change note
17.11.26 accelerometer from sense hat sending data to Python script then port it over to Pd.
Reading Making Music Apps (oreilly)

## OSC communication
[https://github.com/toddtreece/osc-examples.git](https://puredata.info/downloads/osc)
[https://puredata.info/downloads/osc](https://puredata.info/downloads/osc)
get help on routeOSC and packOSC
they are native in Pd - no, actually not native, part of mrpeach which doesn't work with pi

#### 17.12.14
Learning about Live Looping with Ableton using Apogee Gio.


#### 18.02.07
trying pyOSC python library that sends OSC messages, from here http://pdonapi.blogspot.ca/2015/10/using-sensors-in.html

On the pure data side, use a version 0.47 or later and use the [netsend]/[netreceive] and [oscformat]/[oscparse] objects

#### Lots of Pots (shield)
https://moderndevice.com/news/using-the-analog-input-on-the-lots-of-pots-board-for-raspberry-pi/
https://moderndevice.com/wp-content/uploads/2013/07/LotsOfPots.pdf

#### 18.02.10
LOP shield built but not working yet, could be that it's made for older version of RPi, 26pin
also, test the solder connections for connectivity (look at LOP schematic)
#### 18.02.12
looks like the solder is fine, there's a few in the header that could be redone but the connections seem fine using my (iffy) multimeter.


#### 18.02.15
Finally got Lots of Pots working! reinstalled Raspian and
SPI software seems to be working, might test it with a breadboard and ADC MC3008
try building the rpieffectsbox (in software folder)
or this simple spi volume control example
https://learn.adafruit.com/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi/script

more about SPI here:
https://elinux.org/RPi_SPI
http://ipsolutionscorp.com/raspberry-pi-spi-utility/

### 18.02.17
Pedal-Pi in case, cut and drilled case to fit
now working with looper effect running on startup
https://guitarextended.wordpress.com/2012/08/28/running-pd-on-a-headless-raspberry-pi

### 18.02.19
added sensehat py scripts to Loppi repo
make Loppi into synth first then try guitarFX - rpieffectbox (it's in software folder)

### 18.02.25
 started getting lop2osc.py working
18.02.26 getting buttons working on LOP, discovered that pots don't work with Pd, need to bug fix
18.02.27 figured out the bug, can't use udp in python script, got buttons and pots working in py


#### 18.03.03-05
trying to get lop2pd.py and step-vibrato.pd launching on bootup
#### 18.03.06
got it working, had to put the bash script 'pd_startup.sh' into /etc/profile.d/

Next: get buttons connected to functions in Pd - step-vibrato script.
#### 18.04.04 - creating KalimPi
a. figure out looper in Pd
b. figure how to control looper with LotsOfPots
c. figure how to assemble
d. do I need a screen OLED for this project?

#### 18.04.28
trying osc2pd using "socket" low-level UDP
didn't work on OSx


or pyOSC
https://github.com/ptone/pyosc

#### 18.04.29
works on OSx but doesn't seem to work for python3 in pi
works in python2, but gets an error because...
and mrpeach routeOSC not working with PD on pi

#### 18.05.02
kalimPi working but while trying to shoot video for Sound Intensive, board overheated and stopped working. now won’t even startup.

#### 18.05.06
Build Google nSynth Super project with Adan, Eli and Evan
got them working with Pi3v1 not working with Pi3v2
MicroUSB jack broke after using once, but the MicroUSB jack on the Pi seems to work fine, connect a powerboost100, battery and switch. MIDI keyboard only triggers some notes and there’s a delay.
next steps: figure out how to get seamless notes, multi-note?
seems like others in github issues have the same problem with the semi-assembled version of board.
get refund or new board?

#### 18.05.10
After desoldering a new header on LOP and having the same shorting out/no power on both pi and lop board. After hours of resoldering headers and pots found out that board is toast. pulled pots for use elsewhere. I'm going to trash this lop and buy a new one.

#### 18.05.12
figure out how to convert UUID from phones to a sequence of notes for cicadaPi project.
typical UUID OO:EE:BD:DB:16:E1

rhythm, notes, variation
tried Text-to-music project, ruby script reads text from rss feed and sends

#### 18.05.30
nsynth MIDI issue hacking:
sudo service open-nsynth stop

sudo mount -o remount, rw/
now my nsynth isn't working, screen or pots not working, tried firmware again but nothing.
18.05.31
worked on nsynth again, tried to recompile the code with the original MidiThread.cpp file but still getting the same problems.



### SoundPiKit (AudioRigPi)(AudioRpiKit)
a taxonomy of different functions for workshop

| Input  | DSP (PureData)	  | Output  |
|---|---|---|
|mic |  amplify | speaker  |
|sensor(s), buttons, touch strip | synthesize  |  line-out |
|Sensehat  |  sequencer | line-out  |
|Sensehat | looper  |  line-out |
|Pickup & Pots  | looper  |  line-out |
|Device detection  | sequencer  | MIDI/Audio  |
|MIDI device | sequencer  | physical output (marimba) servo motors to mallets  |
|	air pressure	|		|	vibration	|
|water pressure		|		|		|    |

#### 18.05.18
### Create an PD Essentials tutorial
Digital audio
http://write.flossmanuals.net/pure-data/what-is-digital-audio/

array(table), sequencer
random
common audio effects (DSP)
simple synth? envelopes, filters, sawwave generator -> enveloper filter

### Make Pd cheatsheet

Basics:
    1. Digital Audio
    2. Graphical Programming
    3. Interface: nodes - inlets(on top), outlets (outlets)
                    inlets can be hot or cold (left to right) left executes first
                    Edit Play modes
    4. Syntax:
        a. messages, symbols & comments
        b. GUI objects - bang, toggle, number2, vSlider, hSlider, vRadio


### Pd Exercises:
    01 - basic oscillator [osc~] [dac~]
    02 - OSC with variable [vslider] [number]
    03 - Midi Notes to frequency
    04 - hSlider with rounding/integer
    05 - Introducing Array/Table
    06 - Table with Metronome (Metro) (show table as list)
    07 - Downsampling with phasor
    08 - Audio Input
    09 - Potentiometers (hardware communication) pots/buttons from LOP to PD
    10 - Simple synth
    11 - Simple sequencer
    12 - Audio Effect - delay


Parking lot:
    loading audio file
    record audio
    looping

Roadmap:
    look into converting LOP to a analog input (breadboard) for bringing in analog sensors.

    Hacking Pd
    https://makezine.com/2008/11/03/howto-hacking-rjdj-with-p/

or
there's Python-OSC
https://pypi.org/project/python-osc/
https://github.com/attwad/python-osc


on the PD end:
http://write.flossmanuals.net/pure-data/osc/

Arduino Music and Audio Projects

https://projects.raspberrypi.org/en/projects/ultrasonic-theremin
https://learn.adafruit.com/raspberry-pi-open-sound-control/setting-up-your-raspberry-pi

#### SenseHat to PD
Next Steps:
1. Sense Hat with synth & sequencer

2. Ukulele with LOP and step vibrato.pd
done

3. Axoloti synth & case

#### 4. Kalimpi with LOP - looper with octave effects
using Alfaloop -seems robust, midi or keyboard keys to trigger record/overdub
very complex Pd patch, edit is disabled (press x three times to unlock)
open the midi/keys area, dig around for where to send a bang to record and over buttons, feedback up and down, ducking up and down.

#### 18.06.13
In the bottom right corner of main (Alfaloop.pd) is a link to pd stuff - a central hub to all the discrete components.
After watching more Cheetomoskeeto videos I learned that from my button input I need to change the value from a bang to an actual value and I'm doing this in Pd with the Change object.
Then I've put the trigger into the midi_receive.pd and changed the value to 127 which turns the Record mode on/off.
Next try the Over and Feedback values:

#### 18.06.14
feedback and ducking connected to pots now
over btn doesn't stop after
would be useful to turn on a record light on KalimPi
this might help:???

#### 18.05.15
recoded the buttons to work with different logic not a wait loop. Works better but could be improved further.
also, testing the audio, after making a new Pd file called audio-input.pd I found out that the piezo is not connected. will resolder the connect to get both audio sources to mix for sound.
will use two more pots for volume for each pickup.
next, set up the octaver.


#### 18.06.20
use the _PureData/pd-patches/octave-lower-example.pd_
integrate into Alfaloop2.pd and connect with buttons.

Learned that USB Audio module does not have stereo input and will need to get rid of piezo mic on KalimPi, rewire the guitar pickup for input into USB module.
Have it working with mono 1/8 jack but doesn't seem to work with USB Audio.

https://rbnrpi.wordpress.com/raspberry-pi-control-gpio-and-your-pi-camera-using-your-phone/
https://www.youtube.com/watch?v=Kk9KO6Stqp4


5. nSynth
https://github.com/googlecreativelab/open-nsynth-super
built but MIDI input isn't polyphonic or allowing for playing.
Github issue 29 - suggests MIDI over USB, adding ofxMIDI library and recompiling of file.
getting new parts shipped
parts shipped and soldered into place but still the same problem
give up on this for now...

6. Cicadapi - scans for devices and makes musical patterns from device UIDs
make import bluetooth library work in python3
also, getting Pd to intrepret UID codes, shall that conversion be done in Python? or just splitting te original sequence into space delimited for easy
this might give some hints https://github.com/jwktje/langorhythm


7. Wekinator & Pi - machinelearning with pi
- sensor that learns your gestures

8. Hybrid Guitar - use the acoustic qualities of the guitar but add DAW capabilities, fx and looping(bluetooth pedalswitch).
guitar pickups > Pi > Pd > looping > amp > internal speaker

NetPd - (in PureData Patches)
try playing in a networked situation this summer

Webcam > colour to snd conversion > output sonic composition

ForceSensorResistor with RPi tutorial
https://acaird.github.io/computers/2015/01/07/raspberry-pi-fsr

### Write about:
describe the interactions with musical instruments
Stability of the interface, Signal-near representation, Close coupling to interaction, Sonic complexity

Sound for Augmented-Reality
Sound for Human-Robot Interaction

## Ideas for instruments
- simple jitterbot that amplifies/modifies your voice when you talk to it.
- make a looper that you can walk with
- ambient noise capture device - location, image and sound
- handheld auto-tune mic
- ukulele with fx-controlled by accelerometer
- tiny tap tempo metronome
- use wiimote as a controller (https://www.youtube.com/watch?v=rxHIJx-O3iU)


Piano Forte Guitar (guitar with keyboard)

### Creating Research area
- blog (recruite Evan to help with website and social media)
plan out online content - instructions, questions - faq
connect to others doing this work.
use Github as code repo, wiki and pages
- online forum (created talk.sonicinteraction.design Discourse forum, now configure and populate)
- Meetup monthly


## idea: Exquisite Instrument Game
a variations of the Exquisite Corpse game were you create an instrument with a group by passing along an incomplete version of an instrument with a provocation.

interesting links
https://www.bitpi.co/category/raspberrypi/
https://github.com/kasperkamperman/MobileCameraTemplate
https://www.kasperkamperman.com/blog/
http://www.katjaas.nl/home/home.html


#### 18.06.19
Researching Arthur Carabot
https://www.arthurcarabott.com/
https://github.com/acarabott

Yuri Suzuki
http://yurisuzuki.com/design-studio/z-machines
In 2013, Yuri Suzuki Design Studio was asked for initial concept development for Z-Machines, an all robot music band built to perform beyond the capabilities of the most advanced human musicians.

The challenge was to design a system that could play emotionally engaging music while rediscovering conventional instruments.

David Cranmer
http://www.nervoussquirrel.com/
http://www.nervoussquirrel.com/ferrofluid.html

https://contextsequencer.wordpress.com/


Notes on Field Recording
https://www.creativefieldrecording.com/start-here/

http://daily.redbullmusicacademy.com/2017/03/the-art-of-field-recording

OSC
https://en.wikipedia.org/wiki/Open_Sound_Control


Goals of the workshop
Explore ways of creating instruments
Better understand the nuances of how humans interact with instruments
What makes a great instrument - playability, responsiveness, social
Explore the liminal space between digital and analogue


<h3>References</h3>
http://www.instructables.com/id/Pure-Pi-Control-custom-stompbox-effects-on-a-Raspb/
http://www.instructables.com/id/PiMiDi-A-Raspberry-Pi-Midi-Box-or-How-I-Learned-to/
https://guitarextended.wordpress.com/2011/12/12/installing-pure-data/

questions for Discourse
https://www.quora.com/What-data-structures-and-algorithms-are-used-in-programming-for-music-audio-clips

how is ai and machine learning shaping music?
http://www.wired.co.uk/article/how-ai-and-machine-learning-are-shaping-the-future-of-music

http://www.wired.co.uk/article/ai-music-robot-shimon


https://musictechfest.net/
http://www.vahakn.co.uk/


Sonic Interactions Mission
https://musictechfest.net/musictechifesto/

Seeing that the fertility of music technology as a subject that bridges computational, scientific, social scientific and humanistic approaches, we looked for common ground across those areas.

Music technology has never been more exciting. Every day brings new ways to be musical through new software, instruments, devices, platforms and protocols for fans, artists, and organizations. People are experimenting with new ways to perform, collaborate and compose, to listen to their favorite artists and discover new ones, and to share the music they love.

Meaningful innovation is sustainable and just – yet the current landscape of music technology favors short-term profit-making, too often at the expense of deeper cultural concerns. Landfills swell with carelessly-designed consumer electronics, discs, cartridges, instruments, toys and gadgets. Like other cultural workers, many who contribute most to the richness of musical cultures lead increasingly precarious economic lives. But those who stand to profit the most economically have the biggest say in policy discussions. Too often music technologies are used as tools of exclusion rather than inclusion. Because what counts as “music,” “technology,” and “music technology” is unsettled, those with the most power create the most powerful definitions.

We call for technologies to be created with an eye for the long-term. Musical objects should last as long as the materials out of which they are made or they should be modular, recyclable, or transformable. They should be forward-compatible whenever possible. Data must be portable and not bound to a particular company or platform. At the same time, standards must not become coercive. Music is not standard. We must cultivate the freedom to build and use nonstandard tools.


workshop
- explain intention (workshop goals)
- show structure
- theory
- examples (TED)


Reaching out to other Schools
McGill marcelo.wanderley@mcgill.ca


####  July 2018 - Tumo Notes

students thought it was more about programming.
need more women and musicians in the class

went through Pd exercises 1-7 in first class
played a chord at the end of exercises

Day 2
- play music - explain rhythm connect
- connect physical control. (midi keyboard or Push)
- look for game controllers


Day 2 Plan:

Pd Exercises
1. Tables, Graphs and Arrays
http://write.flossmanuals.net/pure-data/arrays-graphs-tables/

http://write.flossmanuals.net/pure-data/sequencer/
challenge: write a 16 note melody, change the tempo with messages.

2. Step sequencer
http://write.flossmanuals.net/pure-data/step-sequencer/

3. AudioFiles

4. MIDI Controller
http://write.flossmanuals.net/pure-data/controlling-the-synth/

Day2 notes:
Today went well.
went through 4 Pd exercises and had them build their own sequences.
Spent too much time letting them find their own audio files.


Day 3
A. RPi - audio and LOP soldering
B. Music - play simple rhythm together
C. Pd Exercises


Pd Exercises
1. Audio input (exercises 12-13) & connecting to LOP board
2. Simple Sequencer and synth (14-15)
3. Delay FX (16)
4. Audio playback manipulation (17)

Day 4
Talked about making the instrument, looked at some ideas.
Played music -
Pd Sequencer

Day 5 Monday
start building instruments
Pd - learn how to make fx

Day 6 Tuesday
Start building instruments
Pretty good day

Day 7 Wednesday
slow to build instruments because of materials
don't know how to add buttons to Pi, buttons have LED and need power
Looked at Sampling again - Pd - fx and sampling

Day 8 Last day to build instruments
if we don't have an instrument for each team -  I will assign the ukelele or Kalimpi to group
Simple drum machine
Sampler- looper
https://www.rebeltech.org/2016/05/18/pure-data-tutorial-2-sampler-looper/
Synth with delay
https://www.rebeltech.org/patch-library/patch/Arp_with_Delay_and_Envelope

Spent a lot of time getting Pi startup script working properly. lots of voodoo
paths, permissions
looks like one group has pd file running, you can hear the mic and fx but python doesn't seem to be communicating even though its running.

Also, spent a lot of time rebuilding files because everyone is altering their version of simple delay, chorus and tremolo.

* for next time, build FX into the file as an abstraction, instead of separate pd file

#### 18.09.01
courses on kadenze
    machine learning for musicians
    reinventing the piano
    concurrence in python


#### 18.09.26
bought new sensors (soft Potentiometers and sliders)
desoldered one pot and connected a soft Potentiometer

look into connecting controllers (midi keyboard,xbox controller, ps controller, and wii remote)
came across https://www.circuito.io/app?components=512,8680,11021

Cheetomoskeeto uses the hid Pd library - https://www.youtube.com/watch?v=HB_oVny33wA

got hid working on pd extended on mac.
but hid doesn't seem to work properly with Pd .48
FB comment says that it needs to be compiled:

#### try this out
https://github.com/avilleret/hid
looks the same as this:
https://puredata.info/downloads/hid/releases/0.7

also there's this...
https://puredata.info/docs/faq/how-can-i-set-permissions-so-hid-can-read-devices-in-gnu-linux


there's also the ctlin object
http://www.pd-tutorial.com/english/ch04s03.html

wii nunchuck adapter
https://www.robotshop.com/en/wiichuck-adapter-arduino.html?gclid=Cj0KCQjwxbzdBRCoARIsACzIK2lxjNh-FKnSq35UGZDdvLkNQhoeGVD5v1Pi5GZkZsJoofF81cQ5BQQaAl5KEALw_wcB

https://computers.tutsplus.com/tutorials/using-a-wii-nunchuck-to-control-python-turtle--cms-20984

https://pimylifeup.com/raspberry-pi-wiimote-controllers/
https://pimylifeup.com/xbox-controllers-raspberry-pi/

Try installing Pd extended on RPI
http://pi.bek.no/pd-ExtendedInstall/

WiringPi
https://github.com/WiringPi/WiringPi-Python
http://wiringpi.com/

https://www.keithmcmillen.com/blog/manipulating-midi-with-pure-data/

## Nunchuck Working
I got a C program reading the Nunchuck (after lots of headaches, one corrupt SD card and many different wiring configs). I used this code:
https://raspberrypi.stackexchange.com/questions/29720/how-do-i-access-the-wii-nunchuck-using-wiringpi

now to get it over to Pd

FluidSynth: http://www.fluidsynth.org/
http://andrewdotni.ch/blog/2015/02/28/midi-synth-with-raspberry-p/

## This looks like promising way to get the MPK mini working
update: got MPK working but the following site will be helpful when automating startup with Pi

https://lucidbeaming.com/blog/tag/synthesizer/
https://github.com/MarquisdeGeek/FluidPi

this is another good site for automating midi startup
http://andrewdotni.ch/blog/2015/02/28/midi-synth-with-raspberry-p/


Soft Synths
https://github.com/zynthian

## came across this, looks good
http://www.earcatching.com/pdconv/

ABLETON tuts
https://blog.kadenze.com/creative-technology/10-ableton-live-tutorials-for-learning-music-production/?utm_source=kadenze_blog&utm_medium=referral&utm_campaign=biweekly_blog_email

theremin with Sonic Pi and ultrasonic sensor
https://projects.raspberrypi.org/en/projects/ultrasonic-theremin


Hey, let's learn React
https://www.taniarascia.com/getting-started-with-react/

https://linuxmusicians.com/

This was helpful: http://tedfelix.com/linux/linux-midi.html
$ cat /proc/asound/cards
brings up the AKAI MPKmini2

do i need to install this?
https://qjackctl.sourceforge.io/

#### 18.10.01
##### Well, that took ages, 5 days to figure out Midi into Pd on Pi!
sudo aconnect 24:0 128:0

24:0 is the client 24: MPKmini2 and :0 is port
128 is the client num for Pd

here's another advanced midi SETUP
https://forum.critterandguitari.com/t/how-to-advanced-midi-setup-3-1/2264/24

to list out USB devices use:
## lsusb

Write a Pd external
https://github.com/pure-data/externals-howto

##### This tutorial helped me install Pd 49
https://forum.pdpatchrepo.info/topic/11626/pd-48-on-raspberry-pi-3/3

Then I noticed that the [hid] object throws an error that says that the ARM architecture is incompatible with the OS. That made me think that the pd_linux file in the library was not compiled for Raspbian Stretch. So I looked at getting the version of Hid library with the source and make files to recompile in for the current ARM64 architecture.


getting xBox controller working on a Mac
https://github.com/360Controller/360Controller/releases

https://github.com/360Controller/360Controller/blob/master/Readme.md#xbox-one-controllers-connected-with-usb

#### 18.10.09
### Creating SD cards for Sonic Interactions Kit for Workshops
usually making duplicates of SD cards starts with copying from the command line:
sudo dd if=/dev/disk2 of=~/Desktop/SonicInteractions-Kit.dmg

but after a 20 minute process there was a dmg file but it didn't work when trying to create a new disk in Etcher.

I remembered that i used a application called ApplePi Baker when I was duplicating SD cards for Mineblock. So I tried that and it worked with out a problem.
https://www.tweaking4all.com/software/macosx-software/macosx-apple-pi-baker/


## Workshop Learning Resources:
PD Floss Manuals
http://write.flossmanuals.net/pure-data/introduction2/

Cheetomoskeeto's youtube channel
https://www.youtube.com/channel/UC-RatzHn1ukuuINLqnbBYeg

##### * idea
Alter the way that the pick hits the string. use spring to have the pick bounce back and forth.


#### 18.10.10 - 30
mom in hospital, no much to work on research, but thinking about a few things:

- other ways of getting sensor data to Pd quicker (more responsive).
- looked into OpenFrameworks to create a script to pull data, maybe quicker and lower overhead

other protocols:
http://www.eclipse.org/paho/

### LEARN OpenFrameworks
https://openframeworks.cc/ofBook/chapters/of_philosophy.html

TCP vs UDP vs osc
https://openframeworks.cc/ofBook/chapters/network.html

GPIO on OpenFrameworks
https://github.com/kashimAstro/ofxGPIO

Cross compiling for RPi
https://forum.openframeworks.cc/t/cross-compiler-for-of-0-9-0-jessie-arm6-rpi1/21336

https://hackaday.com/2016/09/01/how-to-use-docker-to-cross-compile-for-raspberry-pi-and-more/

## not enough good tutorials on this topic above. leaving cross-compiling for now.

#### 18.11.04
### Article about architecture and digital media
https://solidhaptik.ghost.io/architecture-and-new-media-a-survey/

Love this piece by Brian House
https://brianhouse.net/works/quotidian_record/

CMU Making Interactive things
http://mti.code.arc.cmu.edu/2014/

Daito Manabe
http://www.daito.ws/en

Screen Tearing
https://en.wikipedia.org/wiki/Screen_tearing

## Music reminds us that we are connected


### getting Oh Eye working
first need to detect both ADCs (MCP3008)
try this command:
sudo i2cdetect –y 1
nope!

https://elinux.org/Interfacing_with_I2C_Devices#External_Links


#### 2018.11.07
## Taking inventory of Sonic Interactions projects

1. Sensepi (check for updates, create a synth that responds to accelerometer)
2. Nukele (check for updates)
3. Loppi (in pedal box with generative synth on startup)
4. Pedalpi
5. Cicadapi
6. Axoloti
7. n-synth
8. PiSound
9. campi (zero with cam, and cv with synth)

amplipi (hifiberry)



## PiSound with Modep (is amazing)
https://blokas.io/modep/docs/
Mod duo uses LV2 plugins (interesting)

https://www.moddevices.com/blog/2016/09/08/create-lv2-plugin-part-1
http://lv2plug.in/book/

#### 2018.11.8
went to LA for loop
DIY instrument workshop was rubish, the Novalia boards look interesting but what has been made are all pretty lame marketing efforts, with the exception of the IceCube Album cover that had great art and a functional sampler.

https://www.novalia.co.uk/


watch talks from last year:
https://www.ableton.com/en/blog/loop/talks/

Motors, Magnets and Motion: Electronic Music Instruments from the Physical World
https://www.youtube.com/watch?v=hJHwhb99Bzo
Koka Nikoladze
Gijis Glaskes
Alice Eldridge - open ended experimental, tweaking no-fixed-plan exploration

bring together best of digital and physical instrument  making
speaker bolted into back of cello to create a tight coupling of sound source (strings) and output to create feedback loop

Loop talk with Prince producer, Susan Rogers on working with Prince, audio perception, and making a career in music.
Geggy Tah - Greg Kurstin and Tommy Jordan

[Greg Kurstin] | [https://en.wikipedia.org/wiki/Greg_Kurstin]

melody logic:
small intervals sound angry or sad
large interval jumps sound joyful and happy

audio perception
https://plato.stanford.edu/entries/perception-auditory/
auditory perception psychology

Philosophical thinking about perception has focused predominantly on vision. The philosophical puzzle of perception and its proposed solutions have been shaped by a concern for visual experience and visual illusions. Recently, however, other perceptual modalities have attracted attention. In addition to auditory perception and the experience of sound, touch and tactile awareness have generated philosophical interest concerning, for instance, the tactile and proprioceptive experience of space, the objects of touch, whether contact is required for touch, and whether distinct modalities detect pressure, heat, and pain (see, e.g., O'Shaughnessy 1989, Martin 1993, Scott 2001, Fulkerson 2013).

1. TRANSLATE what we have learned from the visual case into terms that apply to other modalities. This approach is relatively conservative. It assumes that vision is representative or paradigmatic and that we have a good understanding of perception that is derived from the case of vision. One example of this kind of approach would be to develop an account of the representational content of auditory experience.

2. EXTEND our vision-based understanding of perception. Non-visual cases might draw attention to new kinds of phenomena that are missing from or not salient in vision. If so, a vision-based account of perception is satisfactory as far as it goes, but it leaves out critical pieces. For example, speech perception, multimodal perception, and flavor perception might involve novel kinds of perceptual phenomena absent from the visual case.

3. CHALLENGE vision-based claims about perception. If falsifying evidence is discovered in non-visual cases, then theorizing beyond vision may force revision of general claims about perception that are supported by vision. For example, if olfactory experience is not diaphanous, the transparency thesis for perceptual experience fails.

read more about Psychoacoustics:

    AudioUI02acoustics-buxton.pdf
    psychoacoustics-book.pdf
    sound-of-innovation-stanford-andrew-j-nelson6271

#### 2018.11.14
## OhEye Board Coding (cntd):

You can use the command find /sys/bus | grep spi in a terminal if you want to view the connected SPI devices. It will show you something a bit like this:

~~~~
pi@raspberrypi ~ $ find /sys/bus | grep spi
    /sys/bus/spi
    /sys/bus/spi/devices
    /sys/bus/spi/devices/spi0.0
    /sys/bus/spi/devices/spi0.1
    /sys/bus/spi/drivers
    /sys/bus/spi/drivers/mcp251x
    /sys/bus/spi/drivers/mcp251x/bind
    /sys/bus/spi/drivers/mcp251x/module
    /sys/bus/spi/drivers/mcp251x/uevent
    /sys/bus/spi/drivers/mcp251x/unbind
    /sys/bus/spi/drivers/spidev
    /sys/bus/spi/drivers/spidev/bind
~~~~

The code to get data from Spi:

~~~~
#!/usr/bin/env python

# MCP3008 connections are:-
# CLK  =>  SCLK  
# DOUT =>  MISO
# DIN  =>  MOSI
# CS   =>  CE0

import spidev
import time
import os
import urllib
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

spi_ce0 = spidev.Spidev()
spi_ce1 = spidev.Spidev()

spi_ce0.open(0,0)
spi_ce1.open(0,1)

def ReadChannel(channel):
    adc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((adc[1]&3)<<8)+adc[2]
return data

sensor1 = 0
sensor2 = 1
sensor3 = 2
sensor4 = 3
sensor5 = 4
sensor6 = 5
sensor7 = 6
sensor8 = 7

sensor9 = 8
sensor10 = 9
sensor11 = 10
sensor12 = 11
sensor13 = 12
sensor14 = 13
sensor15 = 14
sensor16 = 15

delay = 5
~~~~

There's also this...

~~~~
#!/usr/bin/env python

# MCP3008 connections are:-
# CLK  =>  SCLK  
# DOUT =>  MISO
# DIN  =>  MOSI
# CS   =>  CE0

import spidev
import time

spi_ce0 = spidev.Spidev()
spi_ce1 = spidev.Spidev()

spi_ce0.open(0,0)
spi_ce1.open(0,1)


adc1 = spi_ce0.xfer([1,(8+0)<<4,0])
adc2 = spi_ce0.xfer([1,(8+1)<<4,0])
adc3 = spi_ce0.xfer([1,(8+2)<<4,0])
#... add more lines
adc14 = spi_ce1.xfer([1,(8+6)<<4,0])
adc15 = spi_ce1.xfer([1,(8+7)<<4,0])
adc16 = spi_ce1.xfer([1,(8+8)<<4,0])


sensor1 = ((adc1[1]&3)<<8)+adc1[2]
sensor2 = ((adc2[1]&3)<<8)+adc2[2]
sensor3 = ((adc3[1]&3)<<8)+adc3[2]
#... add more lines
sensor14 = ((adc14[1]&3)<<8)+adc14[2]
sensor15 = ((adc15[1]&3)<<8)+adc15[2]
sensor16 = ((adc16[1]&3)<<8)+adc16[2]

delay = 5
~~~~

After a couple of tweaks I settled on the following code which works. Might need to test the performance but data seems to be coming in for all 16 channels.

Would like to optimize the button code next.

~~~~
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

waitTime = .2
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
    values2 = [0]*8

    for i in range(8):
        values[i] = readadc(i)
        values2[i] = readadc2(i)
        message = str(i) + ' ' + str(values[i]) # make a string for use with Pdsend
        message = message + str(i+8) + ' ' + str(values2[i])
        send2Pd(message)

# consider creating a message that has all values in one string rather than separate messages
    print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} '.format(*values))
    print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} '.format(*values2))
#    print(message)
    time.sleep(waitTime)
~~~~

#### 2018.11.16
After speaking with Adan last night I've decided that I'm going to try to get Nsynth working today.

Here's what's wrong with it so far...
1. when it starts up it intermittently doesn't engage the OLED screen, i think it's a connection problem because the RPi to board connection seems to not be sturdy and the RPi board moves.

2. MIDI doesn't seem to work well with the DIN connection and I'd like to try to get the USBMIDI working.

First up, how to get it connected to the net to update.

Disk is readonly by default, here's how you change that:

7. Lock the filesystem (optional)
When you have set up your device and are happy with the configuration, it is advisable to lock the file system to prevent corruption upon a hard power down (i.e. when the power cable is removed from the device). Reconnect the keyboard and screen for these steps.

Open fstab in a text editor

$ sudo vi /etc/fstab
Add ,ro to the root partition to lock the filesystem at next boot:

proc 					/proc           proc    defaults  	        	0 		0
PARTUUID=7762b82d-01 	/boot           vfat    defaults				0 		2
PARTUUID=7762b82d-02 	/               ext4    defaults,noatime,ro 	0 		1
Reboot, and test the filesystem by using touch xyz to create a new file named xyz. You should be denied this if the system is in read-only mode.

To remount as read-write (to make changes), you can remove the ,ro flag from fstab. To make this change temporarily (e.g. to edit some files), you can remount the filesystem as read-write:

$ sudo mount -o remount,rw /
When you restart, the filesystem will once more be read-only. Your instrument is now fully set up – you can proceed to build it into a case and start to make music with it!
_______________________________________

compiles and works with my Akai MPKmini2, playable but you need to bang on keys to get the sound to register, I think I need to tweak some midi settings to make the sound work even with a softer touch. good for now...


Next, let's try to get the nunchuck working with OhEye Board.

#### 18.11.15
got Python reading data from nunchuck, now to get that data sending to Pd

a few resources:
https://www.raspberrypi.org/magpi/wii-nunchucks-raspberry-pi/
https://github.com/Boeeerb/Nunchuck

Stumbled onto this interesting stuff about VR sound with Pd
http://www.matthiaskronlachner.com/?tag=pure-data
and this project
https://github.com/kronihias/mcfx

## OSC Again
Maybe we can try OSC again for this (more of a standard protocol)
https://rbnrpi.wordpress.com/sonic-pi-3-says-hello-to-raspberry-pi-gpio/


*still need to get data from oi2pd.py into Pd
