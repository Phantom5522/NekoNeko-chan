# Class definition for robot

from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, InfraredSensor, TouchSensor
from ev3dev2.button import Button
from ev3dev2.sound import Sound
from time import sleep

# our custom classes
from toolbox import Debug, Config
from claw import Claw
from statemachine import State, Transition, StateMachine
from cross import Cross
from drive import Drive

from toolbox import Debug


class NekoNekoChan(object):
    def __init__(self):
        Config.update()

        self.sound = Sound()

       # sensor values
        self.sensLeft = ColorSensor(INPUT_1)
        self.sensRight = ColorSensor(INPUT_4) # TODO: Sensoren anschließen
        self.sensIR = InfraredSensor(INPUT_2)
        self.sensTouch = TouchSensor(INPUT_3)
        
        self.btn = Button()

        self.sensValues = {}

        
        # Classes for features
        self.drive = Drive()
        self.cross = Cross()
        self.claw = Claw()
        # statemachine
        self.fsm = StateMachine()
       
        # adding States
        
            # Normal Mode States
        self.fsm.addState("followLine").addFunc(self.drive.followLine, self.sensValues)
        self.fsm.addState("brake")

            # Cross States
        self.fsm.addState("checkNextExit").addFunc(self.drive.followLine, self.sensValues)
        self.fsm.addState("findBall").addFunc(self.drive.followLine, self.sensValues)
        self.fsm.getState("findBall").addFunc(self.cross.updateDistance)
        self.fsm.addState("backToCross").addFunc(self.drive.followLine, self.sensValues)
        self.fsm.addState("approachBall").addFunc(self.drive.followLineSlow, self.sensValues)
        # in state diagramm only named exit
        self.fsm.addState("exitCross").addFunc(self.drive.followLine, self.sensValues)
        

        # adding Transitions

            # Normal Mode Transitions
        self.fsm.addTransition("followLine")
        self.fsm.addTransition("brake").addFunc(self.drive.brake)

            # Cross Transitions
        self.fsm.addTransition("checkNextExit","startCross").addFunc(self.claw.releaseClaw).addFunc(self.cross.turn, "right")
        self.fsm.addTransition("checkNextExit","deadEnd").addFunc(self.cross.turn, "skip")          
        self.fsm.addTransition("checkNextExit","backToCross").addFunc(self.cross.turn, "right").addFunc(self.cross.updateTTE)

        self.fsm.addTransition("findBall").addFunc(self.cross.resetDistance)

        self.fsm.addTransition("followLine","exitCrossFromKown")
        self.fsm.addTransition("followLine","exitCrossFromUnkown")

        self.fsm.addTransition("backToCross","withoutBall").addFunc(self.cross.turn, "180").addFunc(self.cross.setTTE)
        self.fsm.addTransition("backToCross","withBall").addFunc(self.claw.closeClaw, True).addFunc(self.cross.turn, "180")

        self.fsm.addTransition("approachBall")

        self.fsm.addTransition("exitCross", "left").addFunc(self.cross.turn, "left")
        self.fsm.addTransition("exitCross", "straight")

        '''
        Debug.print('States:')
        for state in self.fsm.states:
            Debug.print(self.fsm.states[state].name)
        Debug.print('Transitions:')
        for trans in self.fsm.transitions:
            Debug.print(self.fsm.transitions[trans].toState)

        '''

    def checkNoBlue(self):
        hueLeft = self.sensValues["ColorLeft"][0]
        hueRight = self.sensValues["ColorRight"][0]
        return hueLeft < 0.4 and hueLeft > 0.68 and hueRight < 0.4 and hueRight > 0.68

    # implement luminaceValues
    def checkHalfBlue(self):
        hueLeft = self.sensValues["ColorLeft"][0]
        hueRight = self.sensValues["ColorRight"][0]
        return (hueLeft > 0.4 and hueLeft < 0.68) or (hueRight > 0.4 and hueRight < 0.68)    # TODO: measure best threshold for blue values

    def checkWhite(self):
        luminanceLeft = self.sensValues["ColorLeft"][1]
        luminanceRight = self.sensValues["ColorRight"][1]
        return luminanceLeft > 200 and luminanceRight > 200   # TODO: measure best threshold for blue values
        
    def run(self):

        self.fsm.setState("followLine")
        while True:
            # update sensor values
            self.sensValues["ColorLeft"] = self.sensLeft.hls
            self.sensValues["ColorRight"] = self.sensRight.hls
            self.sensValues["IR"] = self.sensIR.proximity
            self.sensValues["Touch"] = self.sensTouch.is_pressed

            # copy current State
            curState = self.fsm.currentState

            #Debug.print(self.sensValues["ColorLeft"], self.sensValues["ColorRight"]) # TODO: find Lightness thresholds

            if self.btn.down:
                sleep(1)
                if self.btn.down:
                    Config.update()
                    self.drive.updateConfig()
                    self.sound.beep()
            elif self.btn.any():
                break

            
            if curState == "followLine":
                if self.checkHalfBlue():
                    self.fsm.transition("toCheckNextExitStartCross")
            elif curState == "checkNextExit":
                if self.checkWhite():
                    self.fsm.transition("toCheckNextExitDeadEnd")
                elif self.checkWhite() == False and self.checkNoBlue():
                    self.fsm.transition("toFindBall")
            elif curState == "findBall":
                if self.claw.hasBall == 1: #A
                    self.fsm.transition("toFollowLineExitCrossFromUnkown")
                elif self.cross.distance < 20: #B TODO: value for thr
                    self.fsm.transition("toBackToCrossWithoutBall")
                elif self.sensValues["IR"] < 80: # TODO: value for thr
                    self.fsm.transition("toApproachBall")
            elif curState == "approachBall":
                if self.sensValues["Touch"]:
                    self.fsm.transition("toBackToCrossWithBall")
            elif curState == "backToCross":
                if self.checkHalfBlue() and self.claw.hasBall: # 1
                    if self.cross.turnsToExit == 1:
                        self.fsm.transition("toExitCrossLeft")
                    elif self.cross.turnsToExit == 2:
                        self.fsm.transition("toExitCrossStraight")
                elif self.checkHalfBlue(): # 2
                    self.fsm.transition("toCheckNextExitBackToCross")
            elif curState == "exitCross":
                if self.checkWhite() == False and self.checkNoBlue():
                    self.fsm.transition("toFollowLineExitCrossFromKown")

            # From any State
            if self.sensValues["ColorLeft"][1] < 10.0 or self.sensValues["ColorRight"][1] < 10.0:
                self.fsm.transition("toBrake")

            
            self.fsm.execute()
            sleep(0.01)
        
