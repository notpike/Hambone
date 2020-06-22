###################################################
# FILE: Numbers.py                                #
# AUTHOR: NotPike                                 #
# Function: Fake numbers station                  #
###################################################

from modules.Module import *
from random import *


class Numbers(Module):

    def __init__(self):

        if(self.env.SECRET != True):
            self.call = Callsign(self.env.CALLSIGN)

        self.voice = Voice(self.env.VOICE_LANGUAGE, self.env.VOICE_SPEED_SLOW) #Slow Talking
        self.tx = TX(self.env.GPIO)

    def task(self):
        setOne = ""
        setTwo = ""
        setThree = ""

        ## Gen random numbers
        for i in range(3):
            setOne += str(randrange(1,10)) + ", "
            setTwo += str(randrange(1,10)) + ", "
            setThree += str(randrange(1,10)) + ", "

        message = (setOne * 3) + ". " + (setTwo * 3) + ". " + (setThree * 3)
        logging.info("Numbers: " + message)
        
        self.voice.buildAudio(message)


    ## Override
    def run(self):
        self.task()
        self.tx.txOn()
        self.voice.playAudio()
        if(self.env.SECRET != True):
            self.call.cw()
        self.tx.txOff()        