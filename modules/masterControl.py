### IMPORT MODULES ###
from modules.audio import *

audio = Audio()

class MasterControl:

    def __init__(self):
        return

    def select(self, pin):
        switcher={
            1 : print("Test PIN"),
            2 : audio.playWav("../wav/StarWars60.wav")

        }
        func=switcher.get(pin,lambda :'Invalid')
        #return func()
