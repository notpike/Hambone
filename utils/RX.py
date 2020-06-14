###################################################
# FILE: rx.py                                     #
# AUTHOR: NotPike                                 #
# Function: Handles audio record, functions       #
#           refered from alijamaliz.              #
#   https://github.com/alijamaliz/DTMF-detector   #
###################################################

from scipy.io import wavfile as wav
import pyaudio
import wave
import logging

## Move back to root directory
import sys
sys.path.append("..")
from env import *


class RX:

    audio = pyaudio.PyAudio()

    def __init__(self, 
                 file="/tmp/file.wav",
                 format=pyaudio.paInt16,
                 channels=1,
                 rate=20000,
                 chunk=1024,
                 time=0.4):

        self.env = ENV()

        self.WAVE_OUTPUT_FILENAME = file
        self.FORMAT = format       # format of sampling 16 bit int
        self.CHANNELS = channels   # number of channels it means number of sample in every sampling
        self.RATE = rate           # number of sample in 1 second sampling
        self.CHUNK = chunk         # length of every chunk
        self.RECORD_SECONDS = time # time of recording in seconds    

    def recordAudio(self):
        if(self.env.RX):
            # start Recording
            stream = self.audio.open(format=self.FORMAT, 
                                    channels=self.CHANNELS,
                                    rate=self.RATE, 
                                    input=True,
                                    frames_per_buffer=self.CHUNK)
            frames = []

            for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
                data = stream.read(self.CHUNK)
                frames.append(data)

            # stop Recording
            stream.stop_stream()
            stream.close()

            # storing voice
            try:
                waveFile = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
                waveFile.setnchannels(self.CHANNELS)
                waveFile.setsampwidth(self.audio.get_sample_size(self.FORMAT))
                waveFile.setframerate(self.RATE)
                waveFile.writeframes(b''.join(frames))
                waveFile.close()
            except:
                logging.critical("RX WAV SAVE FUNCTION FAILED!")
                exit()
        else:
            return

    def killAudio(self):
        if(self.env.RX):
            self.audio.terminate()
        else:
            return