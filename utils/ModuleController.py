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
from modules.Time import *

class ModuleController:

    audio = Audio()
    time = Time()

    def __init__(self):
        return

    def select(self, pin):
        if(pin == "123"):
            print("Test PIN")                    #Test
            return True

        elif(pin == "321"):
            self.audio.playWav("/wav/StarWars3.wav")  #Audio File
            return True

        elif(pin == "666"):
            self.time.readTimeNow()

        else:
            return False                         # Invalid PIN return False        