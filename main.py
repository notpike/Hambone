from utils.dtmf import *
from utils.rx import *
from utils.tx import *

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
            tx.playWav("wav/StarWars60.wav")
        
    rx.killAudio()
    
