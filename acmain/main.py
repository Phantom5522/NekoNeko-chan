#!/usr/bin/env python3
# shebang line above is mandatory for scripts that should be run directly from EV3

# import alles was wir brauchen
from nekoneko_chan import NekoNekoChan
from time import sleep



def main():
    nchan = NekoNekoChan() # create object instance of robot

    nchan.sound.speak('ready')

    while not nchan.btn.any():
        sleep(0.1)

    nchan.sound.beep()
    sleep(1)


    while not nchan.btn.any():
        nchan.followLine()
        sleep(0.01)
    
    nchan.sound.speak('program end')
        

# calibrate sensors

# wait for button press before starting

# line following

# intersection first turn

# detect ball

# collect ball, turn around

# intersection turn = entry turn

# line following

if __name__ == '__main__':
    main()