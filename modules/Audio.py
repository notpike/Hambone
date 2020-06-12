###################################################
# FILE: audio.py                                  #
# AUTHOR: NotPike                                 #
# Function: Audio out class                       #
###################################################

#from playsound import playsound
from utils.TX import *
import time

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