from time import sleep, time
from toolbox import Config

# Ev3dev classes
from ev3dev2.motor import LargeMotor, MediumMotor, MoveSteering
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C

# custom classes
from toolbox import Debug

# PID Controller class
class PIDController(object):
    def __init__(self, kP = 1.0, kI = 0.0, kD = 0.1):
        Config.update()
        self.kP = Config.pidFast[0]
        self.kI = Config.pidFast[1]
        self.kD = Config.pidFast[2]
        self.target = 30
        self.errorLast = 0
        self.errorIntegrated = 0

    def updateConfig(self):
        self.kP = Config.pidFast[0]
        self.kI = Config.pidFast[1]
        self.kD = Config.pidFast[2]


    def update(self, error):

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


        # milliseconds = int(round(time() * 1000))
        # Debug.print(milliseconds)   # TODO: debug print

        return turn

# Class for all movement actions
class Drive(object):
    def __init__(self):
        self.pid = PIDController(kP= 1.0, kI=0.0, kD=0.1)
        
        # motors
        self.steerPair = MoveSteering(OUTPUT_B, OUTPUT_C)
        self.speed = Config.data['pid']['fast']['speed_max']

    def updateConfig(self):
        self.speed = Config.data['pid']['fast']['speed_max']
        self.pid.updateConfig()

    def followLine(self, sensValues):
        #Debug.print('execute drive.followLine()')
        colorLeft = sensValues["ColorLeft"][1] # TODO: HSL? Lichtwert anpassen
        colorRight = sensValues["ColorRight"][1] 
        error = colorLeft - colorRight

        turn = self.pid.update(error)
        self.steerPair.on(turn, self.speed)

    def followLineSlow(self, speed, sensValues):
        colorLeft = sensValues["ColorLeft"][1] # TODO: HSL? Lichtwert anpassen
        colorRight = sensValues["ColorRight"][1] 
        error = colorLeft - colorRight

        turn = self.pid.update(error)
        self.steerPair.on(turn, self.speed)

    def turn(self, direction):
        pass
    
    def brake(self):
        # Debug.print('Emergency Stop: low reflection')
        self.steerPair.off()
            