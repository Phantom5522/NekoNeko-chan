from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, InfraredSensor, TouchSensor
from ev3dev2.motor import LargeMotor, MediumMotor, MoveSteering
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C

from pid import PIDController

# dies ist 1 test
# test
# dies ist ein test der sich gewaschen hat

class NekoNekoChan(object):
    def __init__(self):
        self.controller = PIDController()
        # self.steer

    def followLine(self):
        print(self.controller.pidLoop(10, 2))
