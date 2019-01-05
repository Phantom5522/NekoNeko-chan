# Finite State Machine
from toolbox import Debug

class StateError(Exception):
    pass

class State(object):
        # exeFunction the function runs in the State
        # sensorValues as Dictionary
    def __init__(self, name):
        self.name = name
        self.listFuncs = list()

    def addFunc(self, funcName, *parameters):
        self.listFuncs.append([funcName,*parameters])

    def execute(self):
        if self.listFuncs != []:
            Debug.print('State: {} called {}'.format(self.name, self.listFuncs))
            for funcAsList in self.listFuncs:
               funcAsList[0](*funcAsList[1:])

class Transition(object):
    def __init__(self, toState):
        self.toState = toState
        self.listFuncs = list()

    def addFunc(self, funcName, *parameters):
        self.listFuncs.append([funcName,*parameters])

    def execute(self):
        if self.listFuncs != []:
            for funcAsList in self.listFuncs:
                Debug.print('Transition called function:', funcAsList[0])
                funcAsList[0](*funcAsList[1:])
        

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

