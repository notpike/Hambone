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

    ## MAIN LOOP
    while(True):
        rx.recordAudio()                        # Record Audio
        number = dtmf.dtmfDecode()              # Sample Audio find DTMF Number
        #print(str(number))

        if(str(number) != lastNumber):          # Debounce 
            if(str(number) != "None"):
                pin += str(number)                  # Concat Number to PIN
                print(pin)

                if(mc.select(pin) or len(pin) > 6 or ("*#" in str(pin))): # If PIN is valid, or larger then 6, clear pin
                    pin = ""

        else:
            continue
        
        lastNumber = str(number) 

    rx.killAudio()                              # Stop Audio Recording

if __name__ == "__main__":
    start()

    # ## Weather
    # pin = "777"
    # mc.select(pin)

    # ## Date
    # pin = "666"
    # mc.select(pin)

    # ## Time
    # pin = "999"
    # mc.select(pin)