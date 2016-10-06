#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Fake RPi.GPIO package
'''
#______________________________________________________________________
# imports

#______________________________________________________________________
# globals
BCM = 'BCM'
BOARD = 'BOARD'

OUT = 'OUT'
IN = 'IN'

LOW = 'LOW'
HIGH = 'HIGH'

FALLING = 'FALLING'
RISING = 'RISING'

PUD_UP = 'PUD_UP'
PUD_DOWN = 'PUD_DOWN'

RPI_INFO = {'INFO': 'Fake GPIO, ¬¬', 'P1_REVISION': 'Fake GPIO, ¬¬'}

VERSION = '0.2.0a0'

#______________________________________________________________________
# VERBOSE
VERBOSE = True

#______________________________________________________________________
# functions wrapper/ base fucntion
def print_data(func):
    def verbose(*args, **kwargs):
        if VERBOSE:
            print(func.__name__, args, kwargs)
    return verbose

#______________________________________________________________________
# PWM class
class PWM(object):

    @print_data
    def __init__(self, channel, frequency):
        self.channel = channel
        self.frequency = frequency
        self.dc = 0

    @print_data
    def start(self, dc):
        pass

    @print_data
    def ChangeFrequency(self, freq):
        self.frequency = freq

    @print_data
    def ChangeDutyCycle(self, dc):
        self.dc = dc

    @print_data
    def stop(self):
        pass

#______________________________________________________________________
# functions

@print_data
def setmode(*args, **kwargs):
    pass

@print_data
def setup(*args, **kwargs):
    pass

@print_data
def output(*args, **kwargs):
    pass

@print_data
def input(*args, **kwargs):
    pass

@print_data
def cleanup(*args, **kwargs):
    pass

@print_data
def wait_for_edge(*args, **kwargs):
    pass

@print_data
def event_detected(*args, **kwargs):
    pass

@print_data
def add_event_detect(*args, **kwargs):
    pass

@print_data
def add_event_callback(*args, **kwargs):
    pass

@print_data
def remove_event_detect(*args, **kwargs):
    pass

@print_data
def setwarnings(*args, **kwargs):
    pass
