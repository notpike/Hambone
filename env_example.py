###################################################
# FILE: env.py                                #
# AUTHOR: NotPike                                 #
# Function: Envirement class, vars go here.       #
###################################################

import logging
import pyaudio


class ENV:

    def __init__(self):
        self.CALLSIGN = "HACKER"
        self.GPIO = 17
        self.DEV = False
        self.TX = True
        self.RX = True

        ### Logging ###
        self.LOGGING_LEVEL = logging.INFO
        self.LOGGING_FILE = 'log/event.log'

        ### Record Settings ###
        self.WAVE_OUTPUT_FILENAME = "/tmp/file.wav"
        self.FILE_FORMAT = pyaudio.paInt16 # format of sampling 16 bit int
        self.CHANNELS = 1                  # number of channels it means number of sample in every sampling
        self.RATE = 44100                  # number of sample in 1 second sampling
        self.CHUNK = 3072                  # length of every chunk
        self.RECORD_SECONDS = 0.4          # time of recording in seconds
        self.INDEX = 0   
      
        ### VOICE Utility ###
        self.VOICE_LANGUAGE = 'en-gb'
        self.VOICE_SPEED_SLOW = False 
        self.VOICE_ONLINE = True

        ### WEATHER Module ###
        ## https://openweathermap.org/
        self.OWM_API  = ""
        self.OWM_LOCATION = "Reno,USA"
        self.OWM_ONLINE = True

        ### Numbers Module ###
        self.SECRET = False  # Controls

        ### Parrot ###
        self.PARROT_MAX_RECORD_TIME = 15