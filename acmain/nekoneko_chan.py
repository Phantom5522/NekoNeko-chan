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
        # statemachine
        self.fsm = StateMachine()
        # adding States
        self.fsm.states["followLine"] = State("followLine")
        self.fsm.states["followLine"].addFunc(self.drive.followLine, self.sensValues)
        
        self.fsm.states["brake"] = State("brake")

        self.fsm.states["checkNextExit"] = State("checkNextExit")
        self.fsm.states["checkNextExit"].addFunc(self.drive.followLine, self.sensValues)
        

        # adding Transitions
        self.fsm.transitions["toFollowLine"] = Transition("followLine")
        
        self.fsm.transitions["toBrake"] = Transition("brake")
        self.fsm.transitions["toBrake"].addFunc(self.drive.brake)

    def checkBlue(self):
        hue = self.sensValues["ColorLeft"][0]
        return hue > 0.4 and hue < 0.68     # TODO: measure best threshold for blue values
        
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
            if curState == None:
                self.fsm.transition("toFollowLine")
            elif self.sensValues["ColorLeft"][1] < 10.0 or self.sensValues["ColorRight"][1] < 10.0:
                self.fsm.transition("toBrake")
            elif self.btn.any():
                break
            elif curState.name != "followLine":
                self.fsm.transition("toFollowLine")

                """

            # EmergencyStop TODO: Wert für Abgrund definieren
        #    if self.sensValues["ColorLeft"] == ABGRUND or self.sensValues["ColorRight"] == ABGRUND:
        #        self.fsm.transition("toBrake")

            # if clauses for changing state

                # calibrate sensors

                # wait for button press before starting

                # line following

                # intersection first turn
            # elif self.checkBlue():
            #     self.fsm.transition("toCrossFirstTurn")

                # detect ball

                # collect ball, turn around

                # intersection turn = entry turn
            """


            
            self.fsm.execute()
            sleep(0.01)
        
