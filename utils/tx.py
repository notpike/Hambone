#from gpiozero import LED

class TX:
    
    def __init__(self, gpio=17):
        #self.GPIO = LED(gpio)
        self.GPIO = gpio

##    def txOn(self):
##        self.GPIO.on()
##        return
##
##    def txOff(self):
##        self.GPIO.off()
##        return