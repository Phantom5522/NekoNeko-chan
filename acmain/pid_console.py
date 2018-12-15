#!/usr/bin/env python3

import os
import sys
from time import sleep
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import Button
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.motor import MoveSteering
from ev3dev2.sound import Sound



def debug_print(*args, **kwargs):
    '''Print debug messages to stderr.

    This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=sys.stderr)


def main():
    sensLight = ColorSensor(INPUT_1)
#     sensColor = ColorSensor(INPUT_4)
#     sensColor.mode = sensColor.MODE_COL_COLOR
    btn = Button()
    sound = Sound()
    steerPair = MoveSteering(OUTPUT_B, OUTPUT_C)
    
#     lastColor = sensColor.color_name

    speed = 90
    kP = 2
    kI = 0.1
    kD = 0.5

    target = 30
    error = 0
    lastError = 0
    turn = 0

    errorAccu = 0
    integral = 0

    sound.tone([(400,400,20), (800,800,20)])

    while not btn.any():
            sleep(0.1)

    sound.beep()
    sleep(2)

    debug_print('Error; Proportial; Integral; Derivative; Turn')
    while not btn.any():
        lightValue = sensLight.reflected_light_intensity
        # colorName = sensColor.color_name


        # detect edge
        if lightValue == 0:
                steerPair.off()
                sleep(0.01)
                continue
        
        error = target - lightValue

        errorAccu += error
        derivative = error - lastError

        # limit integral
        if errorAccu > 200:
                errorAccu = 200
        elif errorAccu < -200:
                errorAccu = -200

        # apply gains
        proportional = error * kP
        integral = errorAccu * kI
        derivative *= kD


        # calculate turn value
        turn = proportional + integral + derivative

        # limit turn value
        if turn > 100:
                turn = 100
        elif turn < -100:
                turn = -100

        steerPair.on(int(turn*1), speed)
        debug_print('{}; {}; {}; {}; {}'.format(int(error), int(proportional), int(integral), int(derivative), int(turn)))
        # if lastColor != colorName:
        #         sound.speak(colorName)

        lastError = error       # set current error to lastError at the end of the loop
        # lastColor = sensColor.color_name

        sleep(0.02)




if __name__ == '__main__':
    main()