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
        # self.setWindup(40)

    def updateConfig(self):
        self.setKp(Config.pidFast[0])
        self.setKi(Config.pidFast[1])
        self.setKd(Config.pidFast[2])

# Class for all movement actions
class Drive(object):
    speed = 10.0
    onWhite = False
    curveDirection = 0


    def __init__(self):
        self.pid = PIDController(kP= 1.0, kI=0.0, kD=0.1)
        self.largeMotor = LargeMotor(OUTPUT_B)
        
        # motors
        try:
            self.steerPair = MoveSteering(OUTPUT_B, OUTPUT_C)
        except ev3dev2.DeviceNotFound as e:
            Debug.print("Error:", e)

        # self.speed = Config.data['pid']['fast']['speed_max']

    def updateConfig(self):
        self.speed = Config.data['pid']['fast']['speed_max']
        self.pid.updateConfig()

    def followLine(self, sensValues):
        lumaLeft = sensValues["ColorLeft"][1] # TODO: HSL? Lichtwert anpassen
        lumaRight = sensValues["ColorRight"][1]
        feedback = lumaLeft - lumaRight
        lumaWhite = False

        # Debug.print("onWhite: {}\tmotorPos: {}\t LastFeedback: {}\tLuma: {}".format(self.onWhite, self.largeMotor.position, self.lastFeedback, (lumaLeft,lumaRight)))
        if lumaLeft > 200 and lumaRight > 200:
            lumaWhite = True

        if lumaWhite and not self.onWhite:
            self.onWhite = True
            self.largeMotor.position = 0
        elif lumaWhite and self.largeMotor.position < -185: # distance over white > XY mm
            if self.curveDirection == -1:
                self.driveMillimeters(-100)
                self.bounce("left")
            elif self.curveDirection == 1:
                self.driveMillimeters(-100)
                self.bounce("right")
            self.largeMotor.position = 0
        elif not lumaWhite:
            self.onWhite = False

            self.pid.update(feedback)
            turn = self.pid.output

            if abs(turn) > 40:
                self.speed = Config.pidFastSpeedMin
            elif self.speed < Config.pidFastSpeedMax:
                self.speed = self.speed + 1
            

            # Debug.print("PID output:", round(turn, 1))
            # Debug.print("Speed:", self.speed)

            if turn > 100:
                turn = 100
            elif turn < -100:
                turn = -100

            self.steerPair.on(-turn, -self.speed)

            if lumaLeft > 200 and lumaRight < 200:
                self.curveDirection = 1
            elif lumaLeft < 200 and  lumaRight > 200:
                self.curveDirection = -1
            

    def followLineSlow(self, speed, sensValues):
        lumaLeft = sensValues["ColorLeft"][1] # TODO: HSL? Lichtwert anpassen
        lumaRight = sensValues["ColorRight"][1] 
        feedback = lumaLeft - lumaRight

        self.pid.update(feedback)
        turn = self.pid.output
        if turn > 100:
            turn = 100
        elif turn < -100:
            turn = -100

        self.steerPair.on(-turn, -self.speed)
    
    def bounce(self, action):
        ''' turns almost 180 degrees in given direction
        '''
        def right():
            self.steerPair.on_for_degrees(-100, 20, 157)
        def left():
            self.steerPair.on_for_degrees(100, 20, 157)
        
        if action == "right":
            right()
        elif action == "left":
            left()
        else:
            raise AttributeError("no valid action string given for bounce()")


    def turn(self, action):
        def right():
            self.steerPair.on_for_degrees(-100, 20, 377)
        def left():
            self.steerPair.on_for_degrees(100, 20, 377)
        def reverse():
            self.steerPair.on_for_degrees(100, 20, 725)

        if action == "rightFirst":
            self.driveMillimeters(-50)
            right()
        elif action == "right":
            right()
        elif action == "left":
            self.driveMillimeters(-50)
            left()
        elif action == "skip":
            left()
        elif action == "back180":
            self.driveMillimeters(-175, speed=40)
            reverse()
        elif action == "180":
            reverse()
        else:
            raise AttributeError("no valid action string given for turn()")
            

    
    def brake(self):
        self.steerPair.off()

    def driveMillimeters(self, millimeters, speed = 20):
        self.steerPair.on_for_degrees(0, speed, -1.95*millimeters)
        self.steerPair.wait_until_not_moving()

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

    
