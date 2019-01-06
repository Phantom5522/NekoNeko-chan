# Finite State Machine
from toolbox import Debug

class StateExistError(Exception):
    pass

class TransitionExistError(Exception):
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
            #Debug.print('State: {} called {}'.format(self.name, self.listFuncs))
            for funcAsList in self.listFuncs:
               funcAsList[0](*funcAsList[1:])

class Transition(object):
    def __init__(self, fromState, toState):
        self.fromState = fromState
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

    def addState(self, stateName):
       
        if self.states.__contains__(stateName) == True:
            raise StateExistError("This State name exist already")
        
        self.states[stateName] = State(stateName)
        return self.states[stateName]

    def getState(self, stateName):
        return self.states[stateName]

    def addTransition(self, fromState, toState, nameExtension = ""):
        transitionName = "to" + toState[0].upper() + toState[1:] + nameExtension[0].upper() + nameExtension[1:]
        
        if self.transitions.__contains__(transitionName) == True:
            raise TransitionExistError("This transition name exist already. Use the nameExtension parameter for the transitions to the same State!")
        
        self.transitions[transitionName] = Transition(fromState, toState)
        return self.transitions[transitionName]

    def getTransition(self, transitionName):
        return self.transitions[transitionName]

    def setState(self, stateName):
        self.currentState = self.states[stateName]
        Debug.print("State changed to: " + stateName)
    
    def transition(self, transName):
        self.trans = self.transitions[transName]

    def execute(self):
        if self.trans != None and (self.trans.fromState == self.currentState or self.trans.fromState == self.trans.toState or self.trans.fromState == "anyState"): #TODO: gibt es Probleme nach der Änderung?
            self.trans.execute()
            self.setState(self.trans.toState)
            self.trans = None
        self.currentState.execute()

