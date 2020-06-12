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

    def __init__(self, gpio=17):
        self.tx = TX(gpio)
        return

    def playWav(self, file):
        self.tx.txOn()

        time.sleep(5)
        
        self.tx.txOff()