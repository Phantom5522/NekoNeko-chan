#!/usr/bin/env python3
# shebang line above is mandatory for scripts that should be run directly from EV3

# import alles was wir brauchen
from nekoneko_chan import NekoNekoChan
from time import sleep
from toolbox import Debug


def main():
    nchan = NekoNekoChan() # create object instance of robot
    nchan.sound.tone([(523, 100, 0), (622, 100, 0), (698, 100, 0)]) # on sound
    
    # calibrate color sensors on white surface
    nchan.sound.speak("calibrating")
    nchan.sensLeft.calibrate_white()
    nchan.sensRight.calibrate_white()
    nchan.sound.tone([(698, 100, 0)])


    nchan.sound.speak('ready')
    # wait for button press before starting the challenge
    while not nchan.sensTouch.is_pressed:
         sleep(0.1)

    nchan.sound.tone([(698, 100, 0)])
    sleep(1)

    nchan.run()

    nchan.sound.speak('bye bye')

    nchan.sound.tone([(698, 100, 0), (622, 100, 0), (523, 100, 0)]) # OFF sound


if __name__ == '__main__':
    main()