###################################################
# FILE: RX.py                                     #
# AUTHOR: NotPike                                 #
# Function: espeak and gTTS helper                #
###################################################

import logging
import os
from gtts import gTTS
from pathlib import Path

## Move back to root directory
import sys
sys.path.append("..")
from env import *

class Voice:

    env = ENV()

    def __init__(self,
                 language = env.VOICE_LANGUAGE,
                 slowAudioSpeed = env.VOICE_SPEED_SLOW,
                 online = env.VOICE_ONLINE):

        self.msg = ""
        self.language       = language
        self.slowAudioSpeed = slowAudioSpeed
        self.online         = True 

    def buildAudio(self, msg):
        self.msg = msg
        try:
            audioFile = gTTS(text=msg, 
                            lang=self.language, 
                            slow=self.slowAudioSpeed)

            audioFile.save('/tmp/gtts.mp3')

            ## If size is 0, Voice is offline
            if(Path('/tmp/gtts.mp3').stat().st_size > 0):
                logging.info("Audio Built")
                self.online = True
            else:
                self.online = False
                logging.warning("Voice Offline")          
        except:
            self.online = False
            logging.warning("Voice Offline")


    def playAudio(self):
        if(self.online):
            logging.info("Audio Played")
            os.system("mpg123 /tmp/gtts.mp3")
        else:
            logging.info("Offline Audio Played")
            os.system("echo " + self.msg + " | espeak-ng -g 20 2> /dev/null")