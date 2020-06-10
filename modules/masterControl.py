###################################################
# FILE: masterControl.py                          #
# AUTHOR: NotPike                                 #
# Function: Helper function for module selection. #
#           PIN comes in, function is ran if it   #
#           matches something in select().        #
###################################################

### IMPORT MODULES ###
from modules.audio import *

audio = Audio()

class MasterControl:

    def __init__(self):
        return

    def select(self, pin):
        switcher={
            1 : print("Test PIN"),                      #Test
            2 : audio.playWav("../wav/StarWars60.wav")  #Audio File

        }
        switcher.get(pin,lambda : print('Invalid PIN')) #Run module
