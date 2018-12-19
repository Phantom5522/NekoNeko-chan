import os, sys, json

class Debug(object):

    @staticmethod
    def print(*args, **kwargs):
        '''Print debug messages to stderr.

        This shows up in the output panel in VS Code.
        '''
        print(*args, **kwargs, file=sys.stderr)

class Config(object):
    def __init__(self):
        # create config if not existing
        with open('cfg/config.json') as f:
            self.data = json.load(f)
            self.pidFast = [self.data['pid']['fast']['kP'], self.data['pid']['fast']['kI'], self.data['pid']['fast']['kD']]
            self.pidSlow = [self.data['pid']['slow']['kP'], self.data['pid']['slow']['kI'], self.data['pid']['slow']['kD']]
    
    def update(self):
        self.__init__()

cfg = Config()