from scipy.io import wavfile as wav
import pyaudio
import wave


class RX:

    FORMAT = pyaudio.paInt16 # format of sampling 16 bit int
    CHANNELS = 1 # number of channels it means number of sample in every sampling
    RATE = 20000 # number of sample in 1 second sampling
    CHUNK = 1024 # length of every chunk
    RECORD_SECONDS = 0.4 # time of recording in seconds
    WAVE_OUTPUT_FILENAME = "/tmp/file.wav" # file name

    audio = pyaudio.PyAudio()

    def __init__(self):
        return    

    def recordAudio(self):
        # start Recording
        stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS,
                        rate=self.RATE, input=True,
                        frames_per_buffer=self.CHUNK)
        frames = []

        for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
            data = stream.read(self.CHUNK)
            frames.append(data)

        # stop Recording
        stream.stop_stream()
        stream.close()

        # storing voice
        waveFile = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(self.CHANNELS)
        waveFile.setsampwidth(self.audio.get_sample_size(self.FORMAT))
        waveFile.setframerate(self.RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()


    def killAudio(self):
        self.audio.terminate()

