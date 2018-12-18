import os, sys

class Toolbox(object):

    @staticmethod
    def debug_print(*args, **kwargs):
        '''Print debug messages to stderr.

        This shows up in the output panel in VS Code.
        '''
        print(*args, **kwargs, file=sys.stderr)