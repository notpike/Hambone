###################################################
# FILE: main.py                                   #
# AUTHOR: NotPike                                 #
# Function: main()                                 #
###################################################

## Envirement Variables
try:
    from env import *
    env = ENV()
except ImportError as error:
    print(">>> Missing env.py file. Copy env-example.py to env.py and update variables.")
    exit()

from utils.DTMF import *
from utils.RX import *
from utils.TX import *
from ModuleController import *

mc   = ModuleController(env)
dtmf = DTMF()
rx   = RX()


def start():
    lastNumber = ""
    pin = ""
    loop = 0     ## Timeout timer
    maxLoop = 15 ## Timeout limit

    ## MAIN LOOP
    while(True):
        if(loop >= maxLoop):
            pin = ""
            loop = 0

        rx.recordAudio()                        # Record Audio
        number = dtmf.dtmfDecode()              # Sample Audio find DTMF Number
        #print(str(number))

        if(str(number) != lastNumber):          # Debounce 
            if(str(number) != "None"):
                pin += str(number)              # Concat Number to PIN
                print(">>> PIN: " + pin)
                loop = 0

                if(mc.select(pin) or len(pin) > 6 or ("*#" in str(pin))): # If PIN is valid, or larger then 6, clear pin
                    pin = ""

        else:
            loop += 1
            continue
        
        lastNumber = str(number) 

    rx.killAudio()                              # Stop Audio Recording

if __name__ == "__main__":
    start()