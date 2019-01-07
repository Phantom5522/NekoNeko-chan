#!/usr/bin/env python3
# shebang line above is mandatory for scripts that should be run directly from EV3
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, InfraredSensor, TouchSensor
from ev3dev2.button import Button
from ev3dev2.sound import Sound
from time import sleep
from drive import Drive

from ev3dev2.motor import LargeMotor, MediumMotor, MoveSteering
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C

# our custom classes
from toolbox import Debug, Config

sensLeft = ColorSensor(INPUT_1)
sensRight = ColorSensor(INPUT_4)
sensIR = InfraredSensor(INPUT_2)
sensTouch = TouchSensor(INPUT_3)

steerPair = MoveSteering(OUTPUT_B, OUTPUT_C)

sensLeft.calibrate_white()
sensRight.calibrate_white()

Debug.print("Calibrated White")

measure = False
minHue = 500
maxHue = 0
minLuminance = 500
maxLuminance = 0
minSaturation = 500
maxSaturation = -500

# # 90°
# sleep(2)
# steerPair.on_for_degrees(-100, 20, 377)
# sleep(2)
# steerPair.on_for_degrees(100, 20, 377)
# sleep(2)
# # 180°
# steerPair.on_for_degrees(-100, 20, 735)
# sleep(2)
# steerPair.on_for_degrees(100, 20, 735)

# drive = Drive()

while True:

    # if sensTouch.is_pressed:
    #     sleep(2)
    #     # steerPair.on_for_degrees(0, 20, -97*6)
    #     drive.driveMillimeters(100)
    #     steerPair.on_for_degrees(-100, 20, 377)
    #     drive.driveMillimeters(500)

    '''
    Debug.print("IR Proximity:", sensIR.proximity)
    '''
    if sensTouch.is_pressed and not measure:
        Debug.print("Active")
        measure = True
        sleep(1)

    if sensTouch.is_pressed and measure:
        
        Debug.print("Inactive")
        
        measure = False
        
        Debug.print("Min Hue:", minHue, "Max Hue:", maxHue)
        Debug.print("Min Luminance:", minLuminance, "Max Luminance", maxLuminance)
        Debug.print("Min Saturation: ", minSaturation, "Max Saturation", maxSaturation)

        minHue = 500
        maxHue = 0
        minLuminance = 500
        maxLuminance = 0
        minSaturation = 500
        maxSaturation = -500

        sleep(1)

    if measure:
        sensValue = sensLeft.hls
        
        if sensValue[0] > maxHue:
            maxHue = sensValue[0]
        
        if sensValue[0] < minHue:
            minHue = sensValue[0]

        if sensValue[1] > maxLuminance:
            maxLuminance = sensValue[1]
        
        if sensValue[1] < minLuminance:
            minLuminance = sensValue[1]

        if sensValue[2] > maxSaturation:
            maxSaturation = sensValue[2]
        
        if sensValue[2] < minSaturation:
            minSaturation = sensValue[2]
        

    sleep(0.25)