###################################################
# FILE: audio.py                                  #
# AUTHOR: NotPike                                 #
# Function: Audio out class                       #
###################################################

from playsound import playsound
from utils.tx import *
import time

class Audio:

    tx   = TX()

    def __init__(self):
        return

    def playWav(self, file):
        self.tx.txOn
        time.print("PIN ON")
        (10)
        #playsound(file)
        #self.tx.txOff