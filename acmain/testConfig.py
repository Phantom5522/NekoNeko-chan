#!/usr/bin/env python3

from toolbox import Config, Debug

Debug.print('Hello, i am connected')

Config.update()
Debug.print(Config.data["version"])
