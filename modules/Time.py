###################################################
# FILE: Time.py                                   #
# AUTHOR: NotPike                                 #
# Function: Reads date time using Voice.py        #
###################################################

from datetime import *

## Move back to root directory
import sys
sys.path.append("..")

from utils.TX import *
from utils.Voice import *
from utils.Callsign import *


class Time:

    def __init__(self, call, gpio=17):
        self.tx = TX(gpio)
        self.voice = Voice()
        self.call = Callsign(call)
    
    def readDate(self):

        day = date.today().strftime("%A")
        month = date.today().strftime("%B")
        dayNumber = date.today().strftime("%-d")

        todaysDate = "Today is " + day + " " + month + " " + dayNumber 

        self.voice.buildAudio(todaysDate)
        self.tx.txOn()
        self.voice.playAudio()
        self.call.cw()
        self.tx.txOff()

    def readTime(self):

        hour = datetime.now().strftime("%-I")
        min = datetime.now().strftime("%m")
        pmAm = datetime.now().strftime("%p")

        timeNow = "The time is " + hour + " " + min + " " + pmAm 

        self.voice.buildAudio(timeNow)
        self.tx.txOn()
        self.voice.playAudio()
        self.call.cw()
        self.tx.txOff()


