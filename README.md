## rpi_vx-7r
あの時だ！ :D 

I built a RPi controller for my Yaesu VX-7R handheld so it can activate the PTT and transmit audio without human interaction. It listens for DTMF commands from the transceiver and dose an action accordingly. Think of this as an IRC bot but with a radio! 

This project was the result of an experiment I had seeing if my handheld could work as a POCSAG transmitter. It didn’t work because the VX-7R doesn't support transmitting data at 9600 baud. More or less it took the 2FSK coming from the audio source and modulated it as NFM. Not to throw away a mostly working product I re-purposed my failed experiment so it can be something fun like a fake number station or read the weather.

This program was written for the RPi and Yaesu VX-7R in mind however the core functionality should work for other applications. Mileage may vary if you use other platforms.

## Required Software
```
$ sudo apt update
$ sudo apt install python3-numpy mpg123 cw espeak-ng
$ pip3 install pyaudio scipy gTTS pyowm==2.10.0
```

## Enable NTP Time and change Time Zone
```
$ sudo timedatectl set-ntp True
$ sudo raspi-config 

(raspi-config): Localisation Options --> Change Time Zone
```

## ENV Class
Envirement variables shuch as callsign need to be present before you start the program. Copy env_example.py to env.py and fill in the required information. 
```
$ cp env_example.py env.py
$ nano env.py
```

## Run Program 
```
sudo python3.X main.py
```

## Current DTMF Commands
```
+---------------------+
|   MODULE  |   PIN   |
+---------------------+
| TEST     -->   123  |
| AUDIO Ex -->   054  |
| DATE     -->   3283 |
| TIME     -->   8463 |
| WX       -->   99   |
| CLR PIN  -->   *#   |  
+---------------------+
```

## YAESU VX-7R 2.5MM JACK
 Yaesu handhelds use a 4 point 2.5mm jack for voice, speaker and data. I recycled a broken hand mic while building this so below is the wire coloring correlation and diagram for this jack. Wire colors may vary so always double check with a multimeter.                               

```
+--+   GND       MIC      DATA    SPEAKER
|  +---------+---------+---------+       
|  |         |         |         +----+	 
|  |         |         |         |    |	 
|  |         |         |         +----+  
|  +---------+---------+---------+       
+--+                                     

+---------------------+
| FUNCTION  |  COLOR  |
+---------------------+
| GND     -->   BRAID |
| MIC     -->   WHITE |
| DATA    -->   BLUE  |
| SPEAKER -->   RED   |
+---------------------+
```

## RPi SCHEMATIC                       
For this radio’s PTT to be activated Mic needs a 2.2K ohm resistance to ground. Voice is also being carried over the same line while this resistance is applied so to create this a parallel circuit is needed. This took some creativity to make work because the RPi audio ground and RPi ground are on the same circuit and because I was using a NPN I had to fudge the RPi’s audio in to keep it from shorting. IE, I flipped the RPi’s audio wires so the RPi’s audio line is going into the Yaesu’s ground and vise versa. Below is schematic for this circuit.    

```
                                     +------+    
            +------------------------+PI GND|    
            |                        +------+    
            |    NPN                             
            +---+\|       440Ω       +----------+
            |     +-----+/\/\/\+-----+PI GPIO 17|
            |   +<|                  +----------+
            |   |                                
            |   | 2.2KΩ                          
+-----------+   +/\/\/\+                         
|                      |                         
|  +------------+      |  +--------------------+ 
|  |PI AUDIO OUT+------+--+VX-7R GND BRAID WIRE| 
|  +------------+         +-------------- -----+ 
|                                                
|  +------------+         +--------------------+ 
|  |PI AUDIO GND+--+------+VX-7R MIC WHITE WIRE| 
|  +------------+  |      +--------------------+ 
|                  |                             
+------------------+                             
```
