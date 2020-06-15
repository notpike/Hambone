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

from utils.TX import *
from utils.Voice import *
from utils.Callsign import *


class Numbers:

    def __init__(self, call, secret=False, gpio=17):
        self.secret = secret
        if(self.secret != True):
            self.call = Callsign(call)

        self.voice = Voice()
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
        
        self.voice.buildAudio(message)
        self.tx.txOn()
        self.voice.playAudio()
        if(self.secret != True):
            self.call.cw()
        self.tx.txOff()






