###################################################
# FILE: Weather.py                                #
# AUTHOR: NotPike                                 #
# Function: Envirement class, vars go here.       #
###################################################

import logging

class ENV:

    def __init__(self):
        self.CALLSIGN = "HACKER"
        self.GPIO = 17
        self.DEV = False
        self.TX = True
        self.RX = True
        self.LOGGING_LEVEL = logging.INFO
        self.LOGGING_FILE = 'log/event.log'

        ### OPEN WEATHER MAP ###
        ## https://openweathermap.org/
        self.OWM_API  = ""
        self.OWM_LOCATION = "Reno,USA"

        ### Numbers ###
        self.SECRET = False  # Controls if your Callsign is sent out or not