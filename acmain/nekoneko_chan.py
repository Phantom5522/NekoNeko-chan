# Class definition for robot

from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, InfraredSensor, TouchSensor
from ev3dev2.motor import LargeMotor, MediumMotor, MoveSteering
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.button import Button

# our custom classes
from pid import PIDController
from claw import Claw


class NekoNekoChan(object):
    def __init__(self):
        self.pid = PIDController(kP= 1.0, kI=0.0, kD=0.1)
        self.claw = Claw()
        # sensor values
        self.sensLight = ColorSensor(INPUT_1)
        self.sensColor = ColorSensor(INPUT_4)
        self.btn = Button()
        # motors
        self.steerPair = MoveSteering(OUTPUT_B, OUTPUT_C)
        self.speed = 50

    def followLine(self):
        lightValue = self.sensLight.reflected_light_intensity
        if lightValue == 0:
            self.steerPair.off()
        else:
            turn = self.pid.update(lightValue)
            self.steerPair.on(turn, self.speed)