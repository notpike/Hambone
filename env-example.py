###################################################
# FILE: Weather.py                                #
# AUTHOR: NotPike                                 #
# Function: Envirement class, vars go here        #
###################################################

class ENV:

    def __init__(self):
        self.CALLSIGN = ""

        ### OPEN WEATHER MAP ###
        ## https://openweathermap.org/
        self.OWM_API  = ""
        self.OWM_LOCATION = "Reno,USA"