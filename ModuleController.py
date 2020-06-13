###################################################
# FILE: ModuleController.py                       #
# AUTHOR: NotPike                                 #
# Function: Helper function for module selection. #
#           PIN comes in, function is ran if it   #
#           matches something in select().        #
###################################################

### IMPORT MODULES ###
from modules.Audio import *
from modules.Time import *
from modules.Weather import *


class ModuleController:

    def __init__(self, env):
        self.env = env

        ### DECLARE MODULES ###
        self.audio = Audio(self.env.CALLSIGN)
        self.time = Time(self.env.CALLSIGN)
        self.weather = Weather(self.env.CALLSIGN, self.env.OWM_API)

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
            self.weather.readWeather(self.env.OWM_LOCATION)
            return True

        else:
            return False                         # Invalid PIN return False        