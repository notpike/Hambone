###################################################
# FILE: Time.py                                   #
# AUTHOR: NotPike                                 #
# Function: Reads date time using Voice.py        #
###################################################
import sys
sys.path.append("..")

from utils.TX import *
from utils.Voice import *


class Time:

    tx = TX()
    voice = Voice()

    def __init__(self):
        return
    
    def readTimeNow(self):
        self.voice.buildAudio("w u 7 a n g Test 123")
        self.tx.txOn()
        self.voice.playAudio()
        self.tx.txOff()




