from time import sleep, time
from toolbox import Config
import ev3dev2
import PID

# Ev3dev classes
from ev3dev2.motor import LargeMotor, MediumMotor, MoveSteering
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C

# custom classes
from toolbox import Debug

# Class for PID Controller
class PIDController(PID.PID):
    def __init__(self, kP = 1.0, kI = 0.0, kD = 0.1):
        super(PIDController, self).__init__(kP, kI, kD)
        Config.update()
        self.updateConfig()
        self.SetPoint = 0.0
        self.setSampleTime(0.02)    # 0.02s -> 50 Hz refresh rate

    def updateConfig(self):
        self.setKp(Config.pidFast[0])
        self.setKi(Config.pidFast[1])
        self.setKd(Config.pidFast[2])    

# Class for all movement actions
class Drive(object):
    speed = 10.0

    def __init__(self):
        self.pid = PIDController(kP= 1.0, kI=0.0, kD=0.1)
        self.largeMotor = LargeMotor(OUTPUT_B)
        
        # motors
        try:
            self.steerPair = MoveSteering(OUTPUT_B, OUTPUT_C)
        except ev3dev2.DeviceNotFound as e:
            Debug.print("Error:", e)

        # self.speed = Config.data['pid']['fast']['speed_max']

    def checkBlue(self, sensValues):
        hueLeft = sensValues["ColorLeft"][0]
        hueRight = sensValues["ColorRight"][0]
        lumaLeft = sensValues["ColorLeft"][1]
        lumaRight = sensValues["ColorRight"][1]
        return (hueLeft > 0.5 and hueLeft < 0.65 and lumaLeft > 80 and lumaLeft < 160) and (hueRight > 0.5 and hueRight < 0.65 and lumaRight > 80 and lumaRight < 160)    # TODO: measure best threshold for blue values

    def updateConfig(self):
        self.speed = Config.data['pid']['fast']['speed_max']
        self.pid.updateConfig()

    def followLine(self, sensValues):
        colorLeft = sensValues["ColorLeft"][1] # TODO: HSL? Lichtwert anpassen
        colorRight = sensValues["ColorRight"][1] 
        feedback = colorLeft - colorRight

        self.pid.update(feedback)
        turn = self.pid.output

        if abs(turn) > 10:
            self.speed = Config.pidFastSpeedMin
        elif self.speed < Config.pidFastSpeedMax:
            self.speed = self.speed + 1
        

        Debug.print("PID output:", round(turn, 1))
        Debug.print("Speed:", self.speed)

        if turn > 100:
            turn = 100
        elif turn < -100:
            turn = -100

        

        self.steerPair.on(-turn, -self.speed)

    def followLineSlow(self, speed, sensValues):
        colorLeft = sensValues["ColorLeft"][1] # TODO: HSL? Lichtwert anpassen
        colorRight = sensValues["ColorRight"][1] 
        feedback = colorLeft - colorRight

        self.pid.update(feedback)
        turn = self.pid.output
        if turn > 100:
            turn = 100
        elif turn < -100:
            turn = -100

        self.steerPair.on(-turn, -self.speed)

    def turn(self, action, sensValues = None):
        def enterCross():
            while not self.checkBlue(sensValues):
                self.followLineSlow(10, sensValues)

        def right():
            self.steerPair.on_for_degrees(-100, 20, 377)
        def left():
            self.steerPair.on_for_degrees(100, 20, 377)
        def reverse():
            self.steerPair.on_for_degrees(100, 20, 735)

        if action == "right":
            enterCross()
            self.driveMillimeters(100)
            right()

        elif action == "left":
            enterCross()
            self.driveMillimeters(100)
            left()
        elif action == "skip":
            left()
        elif action == "180":
            self.driveMillimeters(200)
            reverse()
        else:
            raise AttributeError("no valid action string given for turn()")
            

    
    def brake(self):
        self.steerPair.off()

    def driveMillimeters(self, millimeters):
        self.steerPair.on_for_degrees(0, 20, -1.95*millimeters)

    def resetDistance(self):
        self.distance = 0
        self.largeMotor.position = 0

# module test
if __name__ == "__main__":
    Debug.print("Drive Module Test")
    Debug.print("="*40)
    Debug.deltaTime("Modules loaded")
    drive = Drive()
    Debug.deltaTime("init drive object")

    Config.update()

    for i in range(-5, 5):
        drive.pid.update(i*10)
        sleep(0.03)
        Debug.print(drive.pid.output)

    
