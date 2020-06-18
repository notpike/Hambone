###################################################
# FILE: Time.py                                   #
# AUTHOR: NotPike                                 #
# Function: Reads date time using Voice.py        #
###################################################

from datetime import *
import time
import logging

## Move back to root directory
import sys
sys.path.append("..")

from env import *
from utils.TX import *
from utils.Voice import *
from utils.Callsign import *


class Time:

    env = ENV()
    voice = Voice()

    def __init__(self, 
                 call=env.CALLSIGN, 
                 gpio=env.GPIO):
                 
        self.tx = TX(gpio)
        self.call = Callsign(call)
    
    def readDate(self):
        day = date.today().strftime("%A")
        month = date.today().strftime("%B")
        dayNumber = date.today().strftime("%-d")
        year = date.today().strftime("%Y")

        todaysDate = "Today is " + day + " " + month + " " + dayNumber + " " + year 
        logging.info("Date: " + todaysDate)

        self.voice.buildAudio(todaysDate)
        self.tx.txOn()
        self.voice.playAudio()
        self.call.cw()
        self.tx.txOff()

    def readTime(self):
        hour = time.strftime("%-I")
        min = time.strftime("%M")
        pmAm = time.strftime("%p")

        timeNow = "The time is " + hour + " " + min + " " + pmAm
        logging.info("Time: " + timeNow)

        self.voice.buildAudio(timeNow)
        self.tx.txOn()
        self.voice.playAudio()
        self.call.cw()
        self.tx.txOff()


