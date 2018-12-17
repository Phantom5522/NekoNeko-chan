#!/usr/bin/env python3
# shebang line above is mandatory for scripts that should be run directly from EV3

# import alles was wir brauchen
from nekoneko_chan import NekoNekoChan



def main():
    nchan = NekoNekoChan() # create object instance of robot

    nchan.followLine()  # test function call

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