#!/usr/bin/env python3
# shebang line above is mandatory for scripts that should be run directly from EV3

# import alles was wir brauchen
from nekoneko_chan import NekoNekoChan
from time import sleep
from toolbox import Debug



def main():
    nchan = NekoNekoChan() # create object instance of robot

    nchan.sound.tone([(1000, 200, 0), (1200, 150, 0)])


    while not nchan.btn.any():
        sleep(0.1)

    nchan.sound.beep()
    sleep(1)

    Debug.print('no calibration')
    while not nchan.btn.any():
        

        Debug.print(nchan.sensColor.rgb)
        sleep(1)
    
    sleep(1)
    Debug.print('please calibrate')
    while not nchan.btn.any():
        sleep(0.1)

    sleep(1)


    nchan.sensColor.calibrate_white()
    Debug.print('calibrated')

    while not nchan.btn.any():
        

        Debug.print(nchan.sensColor.rgb)
        sleep(1)


    
    nchan.sound.tone([(1200, 150, 0), (1000, 200, 0)])
        

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