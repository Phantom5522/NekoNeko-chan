#!/usr/bin/env python3
# shebang line above is mandatory for scripts that should be run directly from EV3

# import alles was wir brauchen
from nekoneko_chan import NekoNekoChan
from time import sleep
from toolbox import Debug


def main():
    nchan = NekoNekoChan() # create object instance of robot

    nchan.sound.speak('ready')

    while not nchan.btn.any():
         sleep(0.1)

    nchan.sound.beep()
    sleep(1)

    nchan.run()

    nchan.sound.speak('program end')

if __name__ == '__main__':
    main()