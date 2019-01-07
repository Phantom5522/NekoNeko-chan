from toolbox import Debug

class Cross(object):
    def __init__(self):
        self.distance = 0
        self.turnsToExit = 0

    def updateDistance(self):
        #while self.sensIR.proximity > #optWert:
        #    self.drive.followLine
        pass

    def resetDistance(self):
        self.distance = 0

    def setTTE(self):
        self.turnsToExit = 1

    def updateTTE(self):
        if self.turnsToExit > 0:
            self.turnsToExit += 1
