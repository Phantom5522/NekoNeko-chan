from toolbox import Debug

class Cross(object):
    def __init__(self):
        self.turnsToExit = 0

    def setTTE(self):
        self.turnsToExit = 1

    def updateTTE(self):
        if self.turnsToExit > 0:
            self.turnsToExit += 1
