###################################################
# FILE: Module.py                                 #
# AUTHOR: NotPike                                 #
# Function: Parent class of all Modules           #
###################################################
import logging

## Move back to root directory
import sys
sys.path.append("..")

from env import *
from utils.TX import *
from utils.Callsign import *

class Module:

    env = ENV()

    def __init__(self, env=env):
        self.env = env
        self.call = Callsign(self.env.CALLSIGN)
        self.tx = TX(self.env.GPIO)

    ## Module task
    def task(self):
        return

    ## Helper function for task()
    def run(self):
        self.tx.txOn()
        self.task()
        self.tx.txOff()
