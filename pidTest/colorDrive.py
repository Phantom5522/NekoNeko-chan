#!/usr/bin/env python3
from ev3dev2.motor import MoveSteering, OUTPUT_A, OUTPUT_B
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import Button
from time import sleep

cl = ColorSensor(INPUT_1)
btn = Button()
steer_pair = MoveSteering(OUTPUT_A, OUTPUT_B)

target = 25


# while not btn.any():    # Stop program by pressing any button
#     error = target - cl.reflected_light_intensity
#     turn = error * 1.5
#     steer_pair.on(turn, 20)
#     sleep(0.2)

while not btn.any():    # Stop program by pressing any button
    steer_pair.on(0, 50)
    sleep(0.2)