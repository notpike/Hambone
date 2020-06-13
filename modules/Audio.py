###################################################
# FILE: audio.py                                  #
# AUTHOR: NotPike                                 #
# Function: Audio out class                       #
###################################################

import os
import time
import pathlib

## Move back to root directory
import sys
sys.path.append("..")
from utils.TX import *
from modules.Callsign import *


class Audio:

    def __init__(self, call, gpio=17):
        self.call = Callsign(call)
        self.tx = TX(gpio)
        return

    def playWav(self, file):
        self.tx.txOn()
        self.call.cw()
        os.system("aplay " + str(pathlib.Path().absolute()) + file)
        self.tx.txOff()