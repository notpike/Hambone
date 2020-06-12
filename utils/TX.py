###################################################
# FILE: tx.py                                     #
# AUTHOR: NotPike                                 #
# Function: Handles GPIO pins                     #
###################################################

import os

class TX:
    
    def __init__(self, gpio=17):
        self.GPIO = gpio
        if(os.path.isdir("/sys/class/gpio/gpio$GPIO") == False):
            os.system("echo " + str(self.GPIO) + " > /sys/class/gpio/export")
            os.system("echo \"out\" >  /sys/class/gpio/gpio$GPIO/direction")


    def txOn(self):
        os.system("echo \"1\" > /sys/class/gpio/gpio" + str(self.GPIO) + "/value")

    def txOff(self):
        os.system("echo \"0\" > /sys/class/gpio/gpio" + str(self.GPIO) + "/value")
