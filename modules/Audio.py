###################################################
# FILE: audio.py                                  #
# AUTHOR: NotPike                                 #
# Function: Audio out, uses aplay and mpg123      #
###################################################

import os
import time
import pathlib
import logging

## Move back to root directory
import sys
sys.path.append("..")

from utils.TX import *
from utils.Callsign import *


class Audio:

    def __init__(self, call, gpio=17):
        self.call = Callsign(call)
        self.tx = TX(gpio)

    def playWav(self, file):
        print(">>> Playing Wav: " + file)
        logging.info("Playing Wav: " + file)

        self.tx.txOn()
        os.system("aplay " + str(pathlib.Path().absolute()) + file)
        self.call.cw()
        self.tx.txOff()
    
    def playMp3(self, file):
        print(">>> Playing Mp3: " + file)
        logging.info("Playing Mp3: " + file)

        self.tx.txOn()
        os.system("mpg123 " + str(pathlib.Path().absolute()) + file)
        self.call.cw()
        self.tx.txOff()