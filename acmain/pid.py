

class PIDController(object):
    def __init__(self):
        self.lastError = 0

    def pidLoop(self, x, y):
        return x-y
