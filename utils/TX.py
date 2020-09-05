###################################################
# FILE: tx.py                                     #
# AUTHOR: NotPike                                 #
# Function: Handles GPIO pins                     #
###################################################

import logging
import os

## Move back to root directory
import sys
sys.path.append("..")
from env import *


class TX:
    
    env = ENV()

    def __init__(self, gpio=env.GPIO):

        if(self.env.DEV == False and self.env.TX):

            # RPi init
            if(self.env.RPI):
                self.GPIO = gpio
                if(os.path.isdir("/sys/class/gpio/gpio" + str(self.GPIO)) == False):
                    logging.info("INIT GPIO " + str(self.GPIO) + ": OUT")

                    ## Export GPIO
                    stdr = os.system("echo " + str(self.GPIO) + " > /sys/class/gpio/export")
                    if(stdr > 0):
                        logging.critical("FAILED TO INIT GPIO")
                        exit()

                ## Set GPIO to out
                stdr = os.system("echo \"out\" >  /sys/class/gpio/gpio" + str(self.GPIO) + "/direction")
                if(stdr > 0):
                    logging.critical("FAILED TO SET GPIO DIRECTION")
                    exit()

            # CM1xx init
            if(self.env.CM1xx):
                self.CM1xxFile = open(self.env.CM1xx, "wb") # opens a file to the CM1xx hidraw interface that we'll use later on to control TX
                logging.info("CM1xx control channel open")
                
        else:
            logging.info("__init__(): TX FUNCTION DISABLED")

    def txOn(self):
        if(self.env.DEV == False and self.env.TX):

            logging.info("TX ON")

            # RPI TX
            if(self.env.RPI):
                logging.info("TX ON")
                stdr = os.system("echo \"1\" > /sys/class/gpio/gpio" + str(self.GPIO) + "/value")
                if(stdr > 0):
                    logging.critical("FAILED TO START TX")
                    exit()

            #CM1xx TX Off
            if(self.env.CM1xx):
                self.CM1xxFile.write(b"\x00\x00\x04\x04\x00") 
                self.CM1xxFile.flush()
                # this assumes the specific GPIO3 pin, but nearly 99% of setups will be using this pin
                # we also assume it's not inverted. Future improvement would be to generate these messages
                # based on env.

        else:
            logging.info("txOn(): TX FUNCTION DISABLED")


    def txOff(self):
        if(self.env.DEV == False and self.env.TX):

            logging.info("TX OFF")

            # RPI TX Off
            if(self.env.RPI):
                
                stdr = os.system("echo \"0\" > /sys/class/gpio/gpio" + str(self.GPIO) + "/value")
                if(stdr > 0):
                    logging.critical("FAILED TO STOP TX")
                    exit()

            # CM1xx TX Off
            if(self.env.CM1xx):
                self.CM1xxFile.write(b"\x00\x00\x04\x00\x00")
                self.CM1xxFile.flush()
                                    
        else:
            logging.info("txOff(): TX FUNCTION DISABLED")                