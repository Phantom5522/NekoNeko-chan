from time import sleep

# Ev3dev classes
from ev3dev2.motor import LargeMotor, MediumMotor, MoveSteering
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C

# custom classes
from toolbox import Debug

# PID Controller class
class PIDController(object):
    def __init__(self, kP = 1.0, kI = 0.0, kD = 0.1):
        self.kP = kP
        self.kI = kI
        self.kD = kD
        self.target = 30
        self.errorLast = 0
        self.errorIntegrated = 0

    def update(self, lightValue):
        error = self.target - lightValue

        self.errorIntegrated += error

        derivative = error - self.errorLast

        # limit integral
        if self.errorIntegrated > 200:
            self.errorIntegrated = 200
        elif self.errorIntegrated < -200:
            self.errorIntegrated = -200

        # apply gains
        proportional = error * self.kP
        integral = self.errorIntegrated * self.kI
        derivative *= self.kD

        # calculate turn value
        turn = proportional + integral + derivative

        # limit turn value
        if turn > 100:
            turn = 100
        elif turn < -100:
            turn = -100

        self.errorLast = error

        return turn

# Class for all movement actions
class Drive(object):
    def __init__(self):
        self.pid = PIDController(kP= 1.0, kI=0.0, kD=0.1)
        
        # motors
        self.steerPair = MoveSteering(OUTPUT_B, OUTPUT_C)
        self.speed = 50

    def followLine(self, sensValues):
        lightValue = sensValues["ColorLeft"] # TODO: HSL? Lichtwert anpassen
        turn = self.pid.update(lightValue)
        self.steerPair.on(turn, self.speed)
    
    def brake(self):
        self.steerPair.off()
            