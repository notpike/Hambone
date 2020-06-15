###################################################
# FILE: main.py                                   #
# AUTHOR: NotPike                                 #
# Function: main()                                #
###################################################

## Logging
import logging

## Envirement Variables and log config
try:
    from env import *
    env = ENV()
    logging.basicConfig(filename=env.LOGGING_FILE, level=env.LOGGING_LEVEL, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
except ImportError as error:
    from env_example import *
    env = ENV()
    logging.basicConfig(filename=env.LOGGING_FILE, level=env.LOGGING_LEVEL, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
    logging.critical("Missing env.py file. Please copy the env_example.py to env.py and update variables.")
    exit()

## Application Classes
from utils.DTMF import *
from utils.RX import *
from utils.TX import *
from ModuleController import *

def init():
    global mc 
    global dtmf
    global rx

    mc = ModuleController(env)
    dtmf = DTMF()
    rx   = RX()


def start():
    logging.info('### Start ###')

    lastNumber = ""                      # Debounce
    pin = ""
    loop = 0                             # Timeout timer
    maxLoop = 15                         # Timeout limit

    ## MAIN LOOP
    run = True
    while(run):
        if(loop >= maxLoop):             # If timedout, clear pin reset timer
            pin = ""
            loop = 0

        rx.recordAudio()                 # Record Audio, 0.4sec samples
        number = dtmf.dtmfDecode()       # Sample Audio find DTMF Number

        if(str(number) != lastNumber):   # Debounce 
            if(str(number) != "None"):
                pin += str(number)       # Concat Number to PIN
                loop = 0                 # Reset timeout

                logging.info("PIN: " + pin)

                # If PIN is valid or > 6
                if(mc.select(pin) or len(pin) > 6): 
                    pin = ""

        else:
            loop += 1
            continue
        
        lastNumber = str(number) 

    rx.killAudio()                       # Stop Audio Recording
    logging.info('### Stop ###')

if __name__ == "__main__":
    init()
    start()

    # pin = "3283"
    # mc.select(pin)