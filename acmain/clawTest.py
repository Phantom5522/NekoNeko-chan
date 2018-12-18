#!/usr/bin/env python3

from ev3dev2.button import Button
from ev3dev2.sensor import INPUT_2
from ev3dev2.sensor.lego import InfraredSensor, TouchSensor
from ev3dev2.sound import Sound
from claw import Claw
import os, sys
from time import sleep, time
from toolbox import Debug

btn = Button()
sound = Sound()
sensIR = InfraredSensor()
sensTouch = TouchSensor()


sound.beep()

myClaw = Claw()

myClaw.releaseClaw()


defaultDistance = sensIR.proximity

while sensIR.proximity > defaultDistance * 0.9:
    # follow line
    pass

# search ball
while True:
    # debug_print('Abstand: {}'.format(sensIR.proximity * 0.7))
    # 
    sleep(0.5)

sleep(1)

while True:
    if not myClaw.closed and sensTouch.is_pressed:
        myClaw.closeClaw()
        Debug.print('{}: Closed'.format(time()))
        sound.beep()
    elif btn.up:
        myClaw.releaseClaw()
        Debug.print('{}: Released'.format(time()))

        sound.beep()

    elif btn.enter:
        break
    elif btn.down:
        Debug.print(myClaw.closed)
    sleep(0.02)
