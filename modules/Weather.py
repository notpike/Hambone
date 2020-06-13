###################################################
# FILE: Weather.py                                #
# AUTHOR: NotPike                                 #
# Function: OWM class                             #
###################################################

import pyowm
import math

## Move back to root directory
import sys
sys.path.append("..")
from utils.TX import *
from utils.Voice import *
from modules.Callsign import *

class Weather:

    apiKey = "bc44b73b0c596cb6f1eb5a053ef86c02"

    def __init__(self, call, gpio=17):
        self.call = Callsign(call)
        self.tx = TX(gpio)
        self.voice = Voice()
        self.owm = pyowm.OWM(self.apiKey)

    def getWeather(self):
        observation = self.owm.weather_at_place('London,uk')
        w = observation.get_weather()
        
        temp = math.floor((w.get_temperature()['temp'] - 275.15) * (9/5) + 32)
        rh = w.get_humidity()
        windSpeed = w.get_wind()['speed']
        windDirection = w.get_wind()['deg']

        report = "Air temperature, " + temp + ". " + "Relative Humidity, " + rh + ". " + "Wind Speed, " + windSpeed + " Miles Per Hour at, " + windDirection + " degrees."
    
        self.voice.buildAudio(report)
        self.tx.txOn()
        self.call.cw()
        self.voice.playAudio()
        self.tx.txOff()