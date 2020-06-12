###################################################
# FILE: ModuleController.py                       #
# AUTHOR: NotPike                                 #
# Function: Helper function for module selection. #
#           PIN comes in, function is ran if it   #
#           matches something in select().        #
###################################################

## Move back to root directory
import sys
sys.path.append("..")

### IMPORT MODULES ###
from modules.Audio import *

audio = Audio()

class MasterControl:

    def __init__(self):
        return

    def select(self, pin):
        if(pin == 1):
            print("Test PIN"),                      #Test
        elif(pin == 2):
            audio.playWav("/wav/StarWars3.wav")  #Audio File
        else:
            return