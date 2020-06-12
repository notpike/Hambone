###################################################
# FILE: audio.py                                  #
# AUTHOR: NotPike                                 #
# Function: Audio out class                       #
###################################################

import time

## Move back to root directory
import sys
sys.path.append("..")
from utils.TX import *

class Audio:

    def __init__(self):
        self.tx = TX()
        return

    def playWav(self, file):
        self.tx.txOn
        print("PIN ON")
        time.sleep(5)
        #playsound(file)
        self.tx.txOff