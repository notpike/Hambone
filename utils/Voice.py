###################################################
# FILE: rx.py                                     #
# AUTHOR: NotPike                                 #
# Function: gTTS class                            #
###################################################

import logging
import os
from gtts import gTTS
from pathlib import Path

class Voice:

    def __init__(self,
                 language = 'en-gb',
                 slowAudioSpeed = False,):

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
                self.online = True
            else:
                self.online = False
                logging.warning("Voice Offline")          
        except:
            self.online = False
            logging.warning("Voice Offline")


    def playAudio(self):
        if(self.online):
            os.system("mpg123 /tmp/gtts.mp3")
        else:
            os.system("echo " + self.msg + " | espeak-ng -g 20 2> /dev/null")