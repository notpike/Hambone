###################################################
# FILE: Weather.py                                #
# AUTHOR: NotPike                                 #
# Function: OWM API caller, voice to read weather #
#           https://openweathermap.org/           #
###################################################

import pyowm
import math
from Module import *


class Weather(Module):

    def __init__(self):
        self.call = Callsign(self.env.CALLSIGN)
        self.tx = TX(self.env.GPIO)

        self.apiKey = self.env.OWM_API
        self.online = self.env.OWM_ONLINE
        self.location = self.env.OWM_LOCATION


    def task(self):
        try:
            owm = pyowm.OWM(self.apiKey)
            observation = owm.weather_at_place(self.location)
            w = observation.get_weather()
            self.online = True
        except:
            logging.warning("Weather Offline")
            self.online = False

            self.voice.buildAudio("Sorry. The weather is Offline")

        if(self.online):
            temp = round(((w.get_temperature()['temp'] - 275.15) * (9/5) + 32), 1) # K -> F
            rh = w.get_humidity()
            windSpeed = round((w.get_wind()['speed'] * 2.237), 1)                  # MPS -> MPH
            windDirection = w.get_wind()['deg'] 

            report = "Air temperature, " + str(temp) + ". " + "Relative Humidity, " + str(rh) + ". " + "Wind Speed, " + str(windSpeed) + " Miles Per Hour. At " + str(windDirection) + " degrees."
            logging.info("Weather: " + report)

            self.voice.buildAudio(report)
        else:
            return

    ## Override
    def run(self):
        self.task()
        self.tx.txOn()
        self.voice.playAudio()
        self.call.cw()
        self.tx.txOff()
