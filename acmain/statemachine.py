# Finite State Machine
from toolbox import Debug

class StateError(Exception):
    pass

class State(object):
    def __init__(self, execFunc):
        self.execFunc = execFunc
    
    def execute(self):
        self.execFunc()


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
