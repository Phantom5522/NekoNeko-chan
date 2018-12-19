# Class definition for robot

from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, InfraredSensor, TouchSensor
from ev3dev2.motor import LargeMotor, MediumMotor, MoveSteering
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.button import Button
from ev3dev2.sound import Sound

# our custom classes
from toolbox import Debug
from pid import PIDController
from claw import Claw
from statemachine import State, Transition, StateMachine
from cross import Cross


class NekoNekoChan(object):
    def __init__(self):
        
       # sensor values
        self.sensLight = ColorSensor(INPUT_1)
        self.sensColor = ColorSensor(INPUT_4)
        self.btn = Button()

        self.sensorValues = None

        
        # Classes for features
        self.cross = Cross()
        # statemachine
        self.statemachine = StateMachine()
        # adding States
        #self.statemachine.states["followLine"] = State(self.followLine)
        self.statemachine.states["brake"] = State(self.drive.brake, sensorValues)
        self.statemachine.states["crossFirstTurn"] = State(self.cross.firstTurn, sensorValues)
        # adding Transitions
        #self.statemachine.transitions["toFollowLine"] = Transition(self.statemachine.states["followLine"])
        self.statemachine.transitions["toCrossFirstTurn"] = Transition("crossFirstTurn")
        self.statemachine.transitions["toEmergencyStop"] = Transition("emergencyStop")

    def run(self):
        self.sensorValues[""]
        pass