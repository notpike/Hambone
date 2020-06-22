###################################################
# FILE: Audio.py                                  #
# AUTHOR: NotPike                                 #
# Function: Audio out, uses aplay and mpg123      #
###################################################

from Module import *

import os
import time

class Audio(Module):

    def playWav(self, file):
        logging.info("Playing Wav: " + file)
        os.system("aplay " + file)
    
    def playMp3(self, file):
        logging.info("Playing Mp3: " + file)
        os.system("mpg123 " + file)

    #Override
    def task(self, file):
        if(file.endswith('.mp3')):
            self.playMp3(file)
        if(file.endswith('.wav')):
            self.playWav(file)
        else:
            return

    #Override
    def run(self, file):
        self.tx.txOn()
        self.task(file)
        self.call.cw()
        self.tx.txOff()