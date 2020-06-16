###################################################
# FILE: Weather.py                                #
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
        self.LOGGING_LEVEL = logging.INFO
        self.LOGGING_FILE = 'log/event.log'

        ### Record Settings ###
        self.WAVE_OUTPUT_FILENAME = "/tmp/file.wav"
        self.FILE_FORMAT = pyaudio.paInt16 # format of sampling 16 bit int
        self.CHANNELS = 1                  # number of channels it means number of sample in every sampling
        self.RATE = 20000                  # number of sample in 1 second sampling
        self.CHUNK = 1024                  # length of every chunk
        self.RECORD_SECONDS = 0.4          # time of recording in seconds
        self.INDEX = 0   

        ### OPEN WEATHER MAP ###
        ## https://openweathermap.org/
        self.OWM_API  = ""
        self.OWM_LOCATION = "Reno,USA"

        ### Numbers ###
        self.SECRET = False  # Controls if your Callsign is sent out or not