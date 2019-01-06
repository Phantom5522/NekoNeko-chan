# Claw class definition

from ev3dev2.motor import MediumMotor, OUTPUT_A

class Claw(object):
    def __init__(self):
        self.closed = False
        self.hasBall = False
        self.motor = MediumMotor(OUTPUT_A)
    
    def releaseClaw(self):
        self.motor.on(-50)
        self.motor.wait_until_not_moving(timeout=500)
        self.motor.off()
        self.closed = False

    def closeClaw(self, isBallGrab = False):
        self.motor.on(50)
        self.motor.wait_until_not_moving(timeout=500)
        self.motor.off()
        self.closed = True
        if isBallGrab:
            self.hasBall = True

