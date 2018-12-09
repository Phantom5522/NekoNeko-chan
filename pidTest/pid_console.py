#!/usr/bin/env python3

import os
import sys
from time import sleep
from ev3dev2.sensor import INPUT_1, INPUT_3
from ev3dev2.sensor.lego import ColorSensor


def debug_print(*args, **kwargs):
    '''Print debug messages to stderr.

    This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=sys.stderr)


def main():
    color = ColorSensor(INPUT_1)
    kP = 4
    kI = 2
    kD = 0

    target = 35
    error = 0
    lastError = 0
    turn = 0

    integral = 0
    counter = 0

    while True:
        # Proportional
        error = target - color.reflected_light_intensity
        proportional = error * kP

        # integral
        integral = integral + error
        integral = lastError * kI

        counter = counter + 1

        # derivative
        derivative = error - lastError
        derivative *= kD

        turn = proportional + integral + derivative

        #debug_print('Error: {} P: {} I: {} D: {} Turn: {}'.format(error, proportional, integral, derivative, turn))
        debug_print('Counter: {}'.format(counter))

        lastError = error

        sleep(0.5)


if __name__ == '__main__':
    main()