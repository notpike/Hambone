###################################################
# FILE: dtmf.py                                   #
# AUTHOR: NotPike                                 #
# Function: Handles dtmf decoding, functions      #
#           refered from alijamaliz.              #
#   https://github.com/alijamaliz/DTMF-detector   #
###################################################

from scipy.io import wavfile as wav
from scipy.fftpack import fft
import numpy as np
import logging

## Move back to root directory
import sys
sys.path.append("..")
from env import *

class DTMF:

    env = ENV()

    DTMF_TABLE = {
        '1': [1209, 697], '2': [1336, 697], '3': [1477, 697], 'A': [1633, 697],
        '4': [1209, 770], '5': [1336, 770], '6': [1477, 770], 'B': [1633, 770],
        '7': [1209, 852], '8': [1336, 852], '9': [1477, 852], 'C': [1633, 852],
        '*': [1209, 941], '0': [1336, 941], '#': [1477, 941], 'D': [1633, 941],
    } 

     
    def __init__(self, 
                 file=env.WAVE_OUTPUT_FILENAME,
                 rate=env.RATE):
      
        self.WAVE_OUTPUT_FILENAME = file
        self.RATE = rate


    def isNumberInArray(self, array, number):
        offset = 5
        for i in range(number - offset, number + offset):
            if i in array:
                return True
        return False

    def dtmfDecode(self):
        if(self.env.RX):
            # reading voice
            rate, data = wav.read(self.WAVE_OUTPUT_FILENAME)
            # data is voice signal. its type is list(or numpy array)

            # Calculate fourier trasform of data
            FourierTransformOfData = np.fft.fft(data, self.RATE)

            # Convert fourier transform complex number to integer numbers
            for i in range(len(FourierTransformOfData)):
                FourierTransformOfData[i] = int(np.absolute(FourierTransformOfData[i]))

            # Calculate lower bound for filtering fourier trasform numbers
            LowerBound = 20 * np.average(FourierTransformOfData)
            #print("Lower Bond: ", LowerBound)

            # Filter fourier transform data (only select frequencies that X(jw) is greater than LowerBound)
            FilteredFrequencies = []
            for i in range(len(FourierTransformOfData)):
                if (FourierTransformOfData[i] > LowerBound):
                    FilteredFrequencies.append(i)

            # Detect and print pressed button
            for char, frequency_pair in self.DTMF_TABLE.items():
                if (self.isNumberInArray(FilteredFrequencies, frequency_pair[0]) and
                    self.isNumberInArray(FilteredFrequencies, frequency_pair[1])):
                    return char
        else:
            return "None"
