from statemachine import StateMachine
from toolbox import Debug

testStateMachine = StateMachine(["State1","State2","State3"])



testStateMachine.setStateActive("State3")
Debug.print(str(testStateMachine.getState("State2").active))