# Finite State Machine
from toolbox import Debug

class StateError(Exception):
    pass

class State(object):
        # exeFunction the function runs in the State,
        # sensorValues as Dictionary
    def __init__(self, execFunc, sensorValues):
        self.execFunc = execFunc
        self.sensorValues = sensorValues
    
    def execute(self):
        self.execFunc(self.sensorValues)


class Transition(object):
    def __init__(self, toState):
        self.toState = toState

class StateMachine(object):
    def __init__(self):
        
        Debug.print("Initialisiere State-Machine")
        self.states = {}
        self.transitions = {}
        self.currentState = None
        self.trans = None

    def setState(self, stateName):
        self.currentState = self.states[stateName]
    
    def transition(self, transName):
        self.trans = self.transitions[transName]

    def execute(self):
        if self.trans:
            self.setState(self.trans.toState)
            self.trans = None
        self.currentState.execFunc()
