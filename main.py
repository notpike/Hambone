from dtmf import *
from rx import *
from tx import *

dtmf = DTMF()
rx = RX()
tx = TX()

if __name__ == "__main__":

    PIN = "123"

    ## MAIN LOOP
    while(True):
        rx.recordAudio()
        
        code = dtmf.dtmfDecode()
        if(code == "9"):
            tx.playWav("StarWars60.wav")
        
    rx.killAudio()
    
