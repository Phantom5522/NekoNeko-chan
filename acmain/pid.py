# PID Controller class

class PIDController(object):
    def __init__(self):
        self.lastError = 0

    def update(self, x, y):
        return x-y
