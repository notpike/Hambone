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

    # Select function, PIN goes in, function is preformed
    # and returns True if sucessfull so the PIN cal be cleared
    # in main.py.
    def select(self, pin):
        # Test
        if(pin == "123"):
            print(">>> Test PIN")
            return True

        # May 4th be with you
        elif(pin == "054"):
            self.audio.playWav("/wav/StarWars3.wav")  #Audio File
            return True

        # DATE = 3283
        elif(pin == "3283"):
            self.time.readDate()
            return True

        # TIME = 8463
        elif(pin == "8463"):
            self.time.readTime()
            return True

        # WX = 99
        elif(pin == "99"):
            self.weather.readWeather(self.env.OWM_LOCATION)
            return True

        else:
            return False                         # Invalid PIN return False        