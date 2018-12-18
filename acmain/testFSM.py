from statemachine import StateMachine, State, Transition
from toolbox import Debug

def followLine():
    Debug.print("FollowLine")

def cross1():
    Debug.print("Cross1")

def lineBreak():
    Debug.print("Line Break")

testStateMachine = StateMachine()

testStateMachine.states["followLine"] = State(followLine)
testStateMachine.states["cross1"] = State(cross1)
testStateMachine.states["lineBreak"] = State(lineBreak)

testStateMachine.transitions["toFollowLine"] = Transition("followLine")
testStateMachine.transitions["toCross1"] = Transition("cross1")
testStateMachine.transitions["toLineBreak"] = Transition("lineBreak")