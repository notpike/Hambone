###################################################
# FILE: Weather.py                                #
# AUTHOR: NotPike                                 #
# Function: OWM API caller, voice to read weather #
#           https://openweathermap.org/           #
###################################################

import pyowm
import math

## Move back to root directory
import sys
sys.path.append("..")

from utils.TX import *
from utils.Voice import *
from utils.Callsign import *

class Weather:

    def __init__(self, call, api, gpio=17):
        self.call = Callsign(call)
        self.tx = TX(gpio)
        self.voice = Voice()
        self.apiKey = api

    def readWeather(self, location='reno,usa'):
        owm = pyowm.OWM(self.apiKey)
        observation = owm.weather_at_place(location)
        w = observation.get_weather()
        
        temp = math.floor((w.get_temperature()['temp'] - 275.15) * (9/5) + 32)
        rh = w.get_humidity()
        windSpeed = math.floor(w.get_wind()['speed'] * 2.237)
        windDirection = w.get_wind()['deg'] 

        report = "Air temperature, " + str(temp) + ". " + "Relative Humidity, " + str(rh) + ". " + "Wind Speed, " + str(windSpeed) + " Miles Per Hour, at " + str(windDirection) + " degrees."
    
        self.voice.buildAudio(report)
        self.tx.txOn()
        self.voice.playAudio()
        self.call.cw()
        self.tx.txOff()