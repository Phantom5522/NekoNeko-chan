# Finite State Machine
from toolbox import Debug

class StateError(Exception):
    pass

class State(object):
    def __init__(self, stateName):
        self.name = stateName
        self.active = False
        Debug.print("Initialisiere State: " + self.name)

class StateMachine(object):
    def __init__(self, nameArray):

        Debug.print("Initialisiere State-Machine")
        self.States = []
        
        # Adding States
        for name in nameArray:
            self.States.append(State(name))


    def getState(self, name):
        for state in self.States:
            if state.name == name:
                return state
        raise StateError("State not found!")
    
    def setStateActive(self, name):
       
        activeState = self.getState(name)
        
        for state in self.States:
            state.active = False
        
        activeState.active = True

class NekoNekoChan_FSM(StateMachine):
    def __init__(self):
        super.__init__(["followLine","intersectionFirst"])
        self.hasBall = False
        
    def transitionState():
        if