"""
Python fake RPi.GPIO library
Copyright (C) 2020 Luiz Eduardo Amaral <luizamaral306@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
#----------------------------------------------------------------------
# GLOBALS
#----------------------------------------------------------------------
VERBOSE = True
_FAKE = 'Fake GPIO, ¬¬'

BCM = 'BCM'
BOARD = 'BOARD'

IN = 'IN'
OUT = 'OUT'

LOW = 'LOW'
HIGH = 'HIGH'

RISING = 'RISING'
FALLING = 'FALLING'
BOTH = 'BOTH'

PUD_UP = 'PUD_UP'
PUD_DOWN = 'PUD_DOWN'
PUD_OFF = 'PUD_OFF'

HARD_PWM = 'HARD_PWM'
UNKNOWN = 'UNKNOWN'
I2C = 'I2C'
SPI = 'SPI'
SERIAL = 'SERIAL'

RPI_INFO = {
    'P1_REVISION': _FAKE,
    'REVISION': _FAKE,
    'TYPE': _FAKE,
    'MANUFACTURER': _FAKE,
    'PROCESSOR': _FAKE,
    'RAM': _FAKE,
    'INFO': _FAKE,
}
RPI_REVISION = _FAKE

VERSION = '1.0.0'

#----------------------------------------------------------------------
# DECORATORS
#----------------------------------------------------------------------
def log(func):
    def verbose(*args, **kwargs):
        if VERBOSE:
            print(func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return verbose

#----------------------------------------------------------------------
# CLASSES
#----------------------------------------------------------------------
class PWM(object):
    @log
    def __init__(self, channel, frequency):
        self.channel = channel
        self.frequency = frequency
        self.dc = 0

    @log
    def start(self, dc):
        pass

    @log
    def ChangeFrequency(self, freq):
        self.frequency = freq

    @log
    def ChangeDutyCycle(self, dc):
        self.dc = dc

    @log
    def stop(self):
        pass

#----------------------------------------------------------------------
# FUNCTIONS
#----------------------------------------------------------------------
@log
def setmode(*args, **kwargs):
    pass

@log
def getmode(*args, **kwargs):
    pass

@log
def gpio_function(*args, **kwargs):
    pass

@log
def setup(*args, **kwargs):
    pass

@log
def output(*args, **kwargs):
    pass

@log
def input(*args, **kwargs):
    pass

@log
def cleanup(*args, **kwargs):
    pass

@log
def wait_for_edge(*args, **kwargs):
    pass

@log
def event_detected(*args, **kwargs):
    pass

@log
def add_event_detect(*args, **kwargs):
    pass

@log
def add_event_callback(*args, **kwargs):
    pass

@log
def remove_event_detect(*args, **kwargs):
    pass

@log
def setwarnings(*args, **kwargs):
    pass
