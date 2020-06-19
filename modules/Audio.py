###################################################
# FILE: Nudio.py                                  #
# AUTHOR: NotPike                                 #
# Function: Audio out, uses aplay and mpg123      #
###################################################

import os
import time
import pathlib

from Module import *


class Audio(Module):

    def playWav(self, file):
        logging.info("Playing Wav: " + file)
        os.system("aplay " + str(pathlib.Path().absolute()) + file)
        self.call.cw()
    
    def playMp3(self, file):
        logging.info("Playing Mp3: " + file)
        os.system("mpg123 " + str(pathlib.Path().absolute()) + file)
        self.call.cw()

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
        self.tx.txOff()