###################################################
# FILE: main.py                                   #
# AUTHOR: NotPike                                 #
# Function: main.                                 #
###################################################

from utils.dtmf import *
from utils.rx import *
from utils.tx import *
from modules.masterControl import *

dtmf = DTMF()
rx   = RX()
tx   = TX()
mc   = MasterControl()

def start():
    ## MAIN LOOP
    while(True):
        rx.recordAudio()
        
        pin = dtmf.dtmfDecode()
        #pin = 2
        if(pin):
            mc.select(pin)
        
    rx.killAudio()

if __name__ == "__main__":
    start()