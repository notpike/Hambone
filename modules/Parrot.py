###################################################
# FILE: Parrot.py                                 #
# AUTHOR: NotPike                                 #
# Function: Records and replays audio             #
###################################################
from scipy.io import wavfile as wav
import pyaudio
import wave
import threading
import pathlib

from modules.Module import *
from modules.Audio import *

## Move back to root directory
import sys
sys.path.append("..")

from utils.DTMF import *

class Parrot(Module):

    dtmf = DTMF()
    audio = pyaudio.PyAudio()
    mAudio = Audio()
    dtmfSample = ''

    def task(self):
        logging.info("Parrot Start")
        # Instructions
        self.voice.buildAudio(self.env.PARROT_MSG)
        self.tx.txOn()
        self.voice.playAudio()
        self.mAudio.playWav(str(pathlib.Path().absolute()) + "/wav/beep.wav")
        self.tx.txOff()

        # Record
        logging.info("Parrot Start Record")
        self.recordAudio()
        logging.info("Parrot End Record")

        #self.killAudio()

        # Playback
        self.tx.txOn()
        self.mAudio.playWav('/tmp/parrot.wav')
        self.call.cw()
        self.tx.txOff()

        #Logging
        logging.info("Parrot End")

    def recordAudio(self):
        # start Recording
        stream = self.audio.open(format=self.env.FILE_FORMAT, 
                                channels=self.env.CHANNELS,
                                input_device_index=self.env.INDEX,
                                rate=self.env.RATE, 
                                input=True,
                                frames_per_buffer=self.env.CHUNK)

        frames = []
        parrotFrames = []

        maxTime = int(self.env.RATE / self.env.CHUNK * self.env.PARROT_MAX_RECORD_TIME)
        maxTimeCount = 0
        sampleTime = int(self.env.RATE / self.env.CHUNK * self.env.RECORD_SECONDS)
        sampleCount = 0
        stop = '#'
        
        global dtmfSample
        dtmfSample = ''

        while(dtmfSample != stop and maxTime >= maxTimeCount):  #Keep recording untill # or maxttime
            data = stream.read(self.env.CHUNK) #Sample
            frames.append(data)                #Save to DTMF sample
            parrotFrames.append(data)          #Save to Parrot.wav

            sampleCount += 1                   #DTMF Counter
            maxTimeCount +=1                   #Max Time Counter

            # Check DTMF every 0.4 sec of recording
            if(sampleCount >= sampleTime):
                thread = threading.Thread(target=self.decodeDTMF, args=(self.env.WAVE_OUTPUT_FILENAME, frames))
                thread.start()  #Start Thread, Find DTMF Value
                frames = []     #Reset
                sampleCount = 0 #Reset

        # Remove Last chunk to prevent tone from being brodcasted

        # Stop Recording
        stream.stop_stream()
        stream.close()

        # Save Final
        self.saveWav('/tmp/parrot.wav', parrotFrames)

    def decodeDTMF(self,file,frames):
        self.saveWav(file,frames)
        global dtmfSample
        dtmfSample = self.dtmf.dtmfDecode()

    ## Storing Wav
    def saveWav(self,file,frames):
        try:
            waveFile = wave.open(file, 'wb')
            waveFile.setnchannels(self.env.CHANNELS)
            waveFile.setsampwidth(self.audio.get_sample_size(self.env.FILE_FORMAT))
            waveFile.setframerate(self.env.RATE)
            waveFile.writeframes(b''.join(frames))
            waveFile.close()
        except:
            logging.critical("RX WAV SAVE FUNCTION FAILED!")
            exit()

    def killAudio(self):
        if(self.env.RX):
            self.audio.terminate()
        else:
            return  
   
    ## Override
    def run(self):
        self.task()