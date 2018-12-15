#!/usr/bin/env python3

from ev3dev2.button import Button
from ev3dev2.sensor import INPUT_2
from ev3dev2.sensor.lego import InfraredSensor, TouchSensor
from ev3dev2.sound import Sound
from claw import Claw
import os, sys
from time import sleep, time

btn = Button()
sound = Sound()
sensIR = InfraredSensor()
sensTouch = TouchSensor()


sound.beep()

myClaw = Claw()

myClaw.releaseClaw()

def debug_print(*args, **kwargs):
    '''Print debug messages to stderr.

    This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=sys.stderr)


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
        debug_print('{}: Closed'.format(time()))
        sound.beep()
    elif btn.up:
        myClaw.releaseClaw()
        debug_print('{}: Released'.format(time()))

        sound.beep()

    elif btn.enter:
        break
    elif btn.down:
        debug_print(myClaw.closed)
    sleep(0.02)
