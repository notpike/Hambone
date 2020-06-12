###################################################
# FILE: main.py                                   #
# AUTHOR: NotPike                                 #
# Function: main.                                 #
###################################################

from utils.DTMF import *
from utils.RX import *
from utils.TX import *
from utils.ModuleController import *

dtmf = DTMF()
#rx   = RX()
mc   = MasterControl()

def start():
    ## MAIN LOOP
    while(True):
        rx.recordAudio()
        
        pin = dtmf.dtmfDecode()
        if(pin):
            mc.select(pin)
        
    rx.killAudio()

if __name__ == "__main__":
    #start()
    pin = 2
    if(pin):
        mc.select(pin)