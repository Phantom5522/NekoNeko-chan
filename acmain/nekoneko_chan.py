# Class definition for robot

from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, InfraredSensor, TouchSensor
from ev3dev2.button import Button
from ev3dev2.sound import Sound

# our custom classes
from toolbox import Debug
from claw import Claw
from statemachine import State, Transition, StateMachine
from cross import Cross
from dirve import Drive


class NekoNekoChan(object):
    def __init__(self):
        
       # sensor values
        self.sensLeft = ColorSensor(INPUT_1)
        self.sensRight = ColorSensor(INPUT_4)
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
        self.fsm.states["followLine"] = State(self.drive.followLine, self.sensValues)
        self.fsm.states["brake"] = State()
        self.fsm.states["crossFirstTurn"] = State(self.cross.firstTurn, self.sensValues)
        # adding Transitions
        self.fsm.transitions["toFollowLine"] = Transition("followLine")
        self.fsm.transitions["toCrossFirstTurn"] = Transition("crossFirstTurn")
        self.fsm.transitions["toBrake"] = Transition("brake", self.drive.brake)
        
    def run(self):
        while True:
            # update sensor values
            self.sensValues["ColorLeft"] = self.sensLeft.hls
            self.sensValues["ColorRight"] = self.sensRight.hls
            self.sensValues["IR"] = self.sensIR.proximity
            self.sensValues["Touch"] = self.sensTouch.is_pressed

            # copy current State
            curState = self.fsm.currentState

            if self.btn.any():
                break

            # EmergencyStop
        #    if self.sensValues["ColorLeft"] == ABGRUND or self.sensValues["ColorRight"] == ABGRUND:
        #        self.fsm.transition("toBrake")

            # if clauses for changing state

            else:
                self.fsm.transition("toFollowLine")

            
            self.fsm.execute()
        
