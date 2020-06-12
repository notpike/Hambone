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
        return

    def playWav(self, file):
        tx = TX()

        tx.txOn
        time.sleep(5)
        #playsound(file)
        
        tx.txOff