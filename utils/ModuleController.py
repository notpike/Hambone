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
from modules.Weather import *

class ModuleController:

    def __init__(self, callsign):
        self.callsign = callsign

        ### DECLARE MODULES ###
        self.audio = Audio(self.callsign)
        self.time = Time(self.callsign)
        self.weather = Weather(self.callsign)

    def select(self, pin):
        if(pin == "123"):
            print("Test PIN")                    #Test
            return True

        elif(pin == "321"):
            self.audio.playWav("/wav/StarWars3.wav")  #Audio File
            return True

        elif(pin == "666"):
            self.time.readDate()
            return True

        elif(pin == "999"):
            self.time.readTime()
            return True

        elif(pin == "777"):
            self.weather.getWeather()
            return True

        else:
            return False                         # Invalid PIN return False        