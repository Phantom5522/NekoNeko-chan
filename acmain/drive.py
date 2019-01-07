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
        feedback = colorLeft - colorRight

        self.pid.update(feedback)
        turn = self.pid.output
        self.steerPair.on(turn, self.speed)

    def followLineSlow(self, speed, sensValues):
        colorLeft = sensValues["ColorLeft"][1] # TODO: HSL? Lichtwert anpassen
        colorRight = sensValues["ColorRight"][1] 
        feedback = colorLeft - colorRight

        self.pid.update(feedback)
        turn = self.pid.output
        self.steerPair.on(turn, self.speed)

    def turn(self, degrees=0):
        if abs(degrees) > 90:
            raise ValueError("Degrees must be within -90 to 90")
        else:
            steering = degrees / 90 * 50

        self.steerPair.on_for_degrees(steering, 20, 200)
    
    def brake(self):
        self.steerPair.off()


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

    
