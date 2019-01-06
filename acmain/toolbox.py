import os, sys, json
from time import time, sleep

class Debug(object):
    lastTimestamp = round(time()*1000)

    @staticmethod
    def deltaTime(message="no module"):
        curTimestamp = round(time()*1000)
        Debug.print("{}: \t{}".format(curTimestamp - Debug.lastTimestamp, message))
        Debug.lastTimestamp = curTimestamp

    @staticmethod
    def print(*args, **kwargs):
        '''Print debug messages to stderr.

        This shows up in the output panel in VS Code.
        '''
        print(*args, **kwargs, file=sys.stderr)

class Config(object):
    data = dict()
    pidFast = list()
    pidSlow = list()

    @staticmethod
    def update():
        # create config if not existing
        with open('cfg/config.json') as f:
            Config.data = json.load(f)
            Config.pidFast = [Config.data['pid']['fast']['kP'], Config.data['pid']['fast']['kI'], Config.data['pid']['fast']['kD']]
            Config.pidSlow = [Config.data['pid']['slow']['kP'], Config.data['pid']['slow']['kI'], Config.data['pid']['slow']['kD']]
            Debug.print("Config updated")
    

# module test
if __name__ == "__main__":
    Debug.print("Start Test")
    Debug.print("="*40)
    Debug.deltaTime("Time since execution")
    Debug.deltaTime("Time of Debug.print")
    sleep(1)
    Debug.deltaTime("Sleep one second")
