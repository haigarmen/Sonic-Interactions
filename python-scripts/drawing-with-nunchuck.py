from nunchuck import nunchuck
from time import sleep
import turtle

wii = nunchuck()
penstate = 0

turtle.setheading(90)
while True:
    if wii.joystick_y() < 100:
        turtle.backward(10)
    if wii.joystick_y() > 160:
        turtle.forward(10)

    if wii.joystick_x() < 100:
        turtle.left(10)
    if wii.joystick_x() > 160:
        turtle.right(10)

    if wii.button_c() == True:
        turtle.setposition(0,0)
        turtle.setheading(90)
        turtle.clear()
    if wii.button_z() == True:
        if penstate == 0:
            turtle.up()
            penstate = 1
        else:
            turtle.down()
            penstate = 0
        sleep(0.2)
