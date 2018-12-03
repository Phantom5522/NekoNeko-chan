#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM
from time import sleep

target = 50     # light value on edge
error = 0       
lastError = 0   
sLight = 50       # color sensor in reflective mode
steeringValue = 0

proportional = 0
integral = 0
derivative = 0


kP = 1
kI = 1
kD = 1

# Proportional // calculate error
error = target - sLight
proportional = error * kP

# Integral // accumulate error
integral = error + lastError
integral *= kI

# derivative // error - lastError
derivative = error - lastError
derivative *= kD

steeringValue = proportional + integral + derivative
