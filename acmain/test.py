from statemachine import State, Transition, StateMachine
from toolbox import Debug, Config

class Test(object):
        test = 1

testWert = 1

trans = Transition("test",[[Debug.print,"Hallo 1","Hallo 2"],[print]])
trans.addFunc(lambda: print(Test.test))
trans.execute()

print(testWert)