# Finite State Machine
from toolbox import Debug

class StateError(Exception):
    pass

class State(object):
        # exeFunction the function runs in the State
        # sensorValues as Dictionary
    def __init__(self, name, execFunc = None, sensorValues = None):
        self.name = name
        self.execFunc = execFunc
        self.sensorValues = sensorValues
    
    def execute(self):
        if self.execFunc != None and self.sensorValues != None:
            self.execFunc(self.sensorValues)
        elif self.execFunc != None:
            raise Exception("Function has no sensorValues")


class Transition(object):
    def __init__(self, toState, execFunc = None, sensorValues = None):
        self.toState = toState
        self.execFunc = execFunc
        self.sensorValues = sensorValues

    def execute(self):
        if self.execFunc != None and self.sensorValues != None:
            self.execFunc(self.sensorValues)
        elif self.execFunc != None:
            self.execFunc()
        

class StateMachine(object):
    def __init__(self):
        
        Debug.print("Initialize statemachine")
        self.states = {}
        self.transitions = {}
        self.currentState = None
        self.trans = None

    def setState(self, stateName):
        self.currentState = self.states[stateName]
        Debug.print("State changed to: " + stateName)
    
    def transition(self, transName):
        self.trans = self.transitions[transName]

    def execute(self):
        if self.trans != None and self.currentState.name != self.trans.toState:
            self.trans.execute()
            self.setState(self.trans.toState)
            self.trans = None
        self.currentState.execute()

