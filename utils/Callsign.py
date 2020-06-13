###################################################
# FILE: Callsign.py                               #
# AUTHOR: NotPike                                 #
# Function: Helper for cw bin and Voice           #
###################################################

import sys
import os
sys.path.append("..")

from utils.TX import *
from utils.Voice import *

class Callsign:

    def __init__(self, call):
        self.voice = Voice()
        self.call = call

    def readCallsign(self):

        call = " ".join(self.call) 

        self.voice.buildAudio(call)
        self.voice.playAudio()

    def cw(self):
        os.system("echo " + self.call + " | cw -w 20 -t 1200")


