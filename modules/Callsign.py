import sys
import os
sys.path.append("..")

from utils.TX import *
from utils.Voice import *

class Callsign:

    tx = TX()
    voice = Voice()

    def __init__(self, call):
        self.call = call

    def readCallsign(self):

        call = " ".join(self.call) 

        self.voice.buildAudio(call)
        #self.tx.txOn()
        self.voice.playAudio()
        #self.tx.txOff()

    def cw(self):
        #self.tx.txOn()
        os.system("cw " + self.call)
        #self.tx.txOff()


