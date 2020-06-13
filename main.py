###################################################
# FILE: main.py                                   #
# AUTHOR: NotPike                                 #
# Function: main.                                 #
###################################################

from utils.DTMF import *
from utils.RX import *
from utils.TX import *
from utils.ModuleController import *

callsign = "WU7ANG"


dtmf = DTMF()
rx   = RX()
mc   =  ModuleController(callsign)

def start():
    lastNumber = ""
    pin = ""

    ## MAIN LOOP
    while(True):
        rx.recordAudio()                         # Record Audio
        number = dtmf.dtmfDecode()               # Sample Audio find DTMF Number
        
        if(str(number) != lastNumber):           # Debounce 
            pin += str(number)                   # Concat Number to PIN

            if(mc.select(pin) or len(pin) > 6): # If PIN is valid, or larger then 6, clear pin
                pin = ""

        else:
            continue
        
        lastNumber = str(number) 

    rx.killAudio()                                # Stop Audio Recording

if __name__ == "__main__":
    #start()
    pin = "666"
    mc.select(pin)