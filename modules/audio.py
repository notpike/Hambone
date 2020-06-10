###################################################
# FILE: audio.py                                  #
# AUTHOR: NotPike                                 #
# Function: Audio out class                       #
###################################################

from playsound import playsound

class Audio:

    def __init__(self):
        return

    def playWav(self, file):
        playsound(file)
