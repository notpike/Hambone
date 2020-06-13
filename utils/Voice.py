###################################################
# FILE: rx.py                                     #
# AUTHOR: NotPike                                 #
# Function: gTTS class                            #
###################################################

import os
from gtts import gTTS

class Voice:

    def __init__(self,
                 language = 'en',
                 slowAudioSpeed = False,):

        self.language       = language
        self.slowAudioSpeed = slowAudioSpeed

    def buildAudio(self, msg):
        audioFile = gTTS(text=msg, 
                         lang=self.language, 
                         slow=self.slowAudioSpeed)

        audioFile.save('/tmp/gtts.mp3')


    def playAudio(self):
        os.system("mpg123 /tmp/gtts.mp3")