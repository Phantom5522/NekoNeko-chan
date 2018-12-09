#!/usr/bin/env python3

import os
import sys
from time import sleep
from ev3dev2.sensor import INPUT_1, INPUT_3

def debug_print(*args, **kwargs):
    '''Print debug messages to stderr.

    This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=sys.stderr)


def main():
    debug_print('Henlo, I am AutoCAT')


if __name__ == '__main__':
    main()