###################################################
# FILE: Numbers.py                                #
# AUTHOR: NotPike                                 #
# Function: Fake numbers station                  #
###################################################

from random import *
import logging

## Move back to root directory
import sys
sys.path.append("..")

from env import *
from utils.TX import *
from utils.Voice import *
from utils.Callsign import *


class Numbers:

    env = ENV()

    def __init__(self, 
                 call=env.CALLSIGN, 
                 secret=env.SECRET, 
                 gpio=env.GPIO):

        self.secret = secret
        if(self.secret != True):
            self.call = Callsign(call)

        self.voice = Voice(self.env.VOICE_LANGUAGE, self.env.VOICE_SPEED_SLOW) #Slow Talking
        self.tx = TX(gpio)

    def numbers(self):
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
        self.tx.txOn()
        self.voice.playAudio()
        if(self.secret != True):
            self.call.cw()
        self.tx.txOff()
        