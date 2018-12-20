#!/usr/bin/env python3

from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1
from ev3dev2.sound import Sound
from toolbox import Config, Debug
from time import sleep

Debug.print('Hello, i am connected')

Config.update()
sound = Sound()
Debug.print("JSON Version:", Config.data["version"])

color = ColorSensor()
color.calibrate_white()

while True:
    Debug.print(color.hls)
    hue = color.hls[0]

    if hue > 0.4 and hue < 0.68:
        sound.speak("dah be dee, dah be dye")
        sleep(1)
    elif hue > 0.8 or hue < 0.2:
        sound.speak("red")
        sleep(1)
    elif hue > 0.65:
        sound.speak("white")
        sleep(1)

    sleep(0.1)