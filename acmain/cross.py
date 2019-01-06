from toolbox import Debug

class Cross(object):
    def __init__(self):
        self.distance = 0
        self.turnsToExit = 0

    def firstTurn(self, sensorValues):
        Debug.print("Robo at Cross first Turn")