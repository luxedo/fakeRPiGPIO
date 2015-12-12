#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Fake RPi GPIO

'''
BCM = 'BCM'
OUT = 'OUT'
RPI_INFO = {'INFO': 'Fake GPIO, ¬¬', 'P1_REVISION': 'Fake GPIO, ¬¬'}

VERBOSE = False

def show_data(name, *args, **kwargs):
    if VERBOSE:
        print(name, ': ', args, kwargs)

def setmode(*args, **kwargs):
    show_data('setmode', *args, **kwargs)

def setup(*args, **kwargs):
    show_data('setup', *args, **kwargs)

def output(*args, **kwargs):
    show_data('output', *args, **kwargs)

def input(*args, **kwargs):
    show_data('input', *args, **kwargs)

def cleanup(*args, **kwargs):
    show_data('cleanup', *args, **kwargs)
