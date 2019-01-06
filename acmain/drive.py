from time import sleep, time
from toolbox import Config
import ev3dev2
import PID

# Ev3dev classes
from ev3dev2.motor import LargeMotor, MediumMotor, MoveSteering
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C

# custom classes
from toolbox import Debug

class wrappedPID(PID.PID):
    pass

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

        # Debug.deltaTime("PID Update") # TODO: measure execution time

        return turn

# Class for all movement actions
class Drive(object):
    def __init__(self):
        self.pid = PIDController(kP= 1.0, kI=0.0, kD=0.1)
        
        # motors
        try:
            self.steerPair = MoveSteering(OUTPUT_B, OUTPUT_C)
        except ev3dev2.DeviceNotFound as e:
            Debug.print("Error:", e)

        self.speed = Config.data['pid']['fast']['speed_max']

    def updateConfig(self):
        self.speed = Config.data['pid']['fast']['speed_max']
        self.pid.updateConfig()

    def followLine(self, sensValues):
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

    def turn(self, degrees=0):
        pass
    
    def brake(self):
        self.steerPair.off()


# module test
if __name__ == "__main__":
    Debug.print("Drive Module Test")
    Debug.print("="*40)
    Debug.deltaTime("Modules loaded")
    drive = Drive()
    Debug.deltaTime("init drive object")
    # for i in range(10):
    #     drive.pid.update(i*100)
    newPID = wrappedPID()
    Debug.deltaTime("init ivPID object")
    # newPID.update(10)
    Debug.print(newPID.sample_time)

    
