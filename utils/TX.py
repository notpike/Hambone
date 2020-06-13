###################################################
# FILE: tx.py                                     #
# AUTHOR: NotPike                                 #
# Function: Handles GPIO pins                     #
###################################################

import os


class TX:
    
    def __init__(self, gpio=17):
        self.GPIO = gpio
        if(os.path.isdir("/sys/class/gpio/gpio" + str(self.GPIO)) == False):
            print(">>> INIT GPIO " + str(self.GPIO) + ": OUT")
            os.system("echo " + str(self.GPIO) + " > /sys/class/gpio/export")

        os.system("echo \"out\" >  /sys/class/gpio/gpio" + str(self.GPIO) + "/direction")

    def txOn(self):
        print(">>> TX ON")
        os.system("echo \"1\" > /sys/class/gpio/gpio" + str(self.GPIO) + "/value")

    def txOff(self):
        print(">>> TX OFF")
        os.system("echo \"0\" > /sys/class/gpio/gpio" + str(self.GPIO) + "/value")
