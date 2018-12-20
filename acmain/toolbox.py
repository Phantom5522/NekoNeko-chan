import os, sys, json

class Debug(object):

    @staticmethod
    def print(*args, **kwargs):
        '''Print debug messages to stderr.

        This shows up in the output panel in VS Code.
        '''
        print(*args, **kwargs, file=sys.stderr)

class Config(object):
    data = {}
    pidFast = []
    pidSlow = []

    @staticmethod
    def update():
        # create config if not existing
        with open('cfg/config.json') as f:
            Config.data = json.load(f)
            Config.pidFast = [Config.data['pid']['fast']['kP'], Config.data['pid']['fast']['kI'], Config.data['pid']['fast']['kD']]
            Config.pidSlow = [Config.data['pid']['slow']['kP'], Config.data['pid']['slow']['kI'], Config.data['pid']['slow']['kD']]
            Debug.print("Config updated")
    

