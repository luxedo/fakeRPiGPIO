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
# ----------------------------------------------------------------------
# GLOBALS
# ----------------------------------------------------------------------
VERBOSE = True
_FAKE = "Fake GPIO, ¬¬"

BCM = "BCM"
BOARD = "BOARD"

IN = "IN"
OUT = "OUT"

LOW = "LOW"
HIGH = "HIGH"

RISING = "RISING"
FALLING = "FALLING"
BOTH = "BOTH"

PUD_UP = "PUD_UP"
PUD_DOWN = "PUD_DOWN"
PUD_OFF = "PUD_OFF"

HARD_PWM = "HARD_PWM"
UNKNOWN = "UNKNOWN"
I2C = "I2C"
SPI = "SPI"
SERIAL = "SERIAL"

RPI_INFO = {
    "P1_REVISION": _FAKE,
    "REVISION": _FAKE,
    "TYPE": _FAKE,
    "MANUFACTURER": _FAKE,
    "PROCESSOR": _FAKE,
    "RAM": _FAKE,
    "INFO": _FAKE,
}
RPI_REVISION = _FAKE

VERSION = "1.0.0"

_mode = None
_gpio_bcm_modes = [IN if i < 34 else UNKNOWN for i in range(54)]
_gpio_bcm_modes[14] = SERIAL
_gpio_bcm_modes[15] = SERIAL
_gpio_bcm_modes[29] = OUT
_gpio_board_modes = {
    3: IN,
    5: IN,
    7: IN,
    8: SERIAL,
    10: SERIAL,
    11: IN,
    12: IN,
    13: IN,
    15: IN,
    16: IN,
    18: IN,
    19: IN,
    21: IN,
    22: IN,
    23: IN,
    24: IN,
    26: IN,
    29: IN,
    31: IN,
    32: IN,
    33: IN,
    35: IN,
    36: IN,
    37: IN,
    38: IN,
    40: IN,
}
_gpio_modes = _gpio_bcm_modes.copy()
_gpio_default_states = [LOW for i in range(54)]
_gpio_states = _gpio_default_states[:]

# ----------------------------------------------------------------------
# DECORATORS
# ----------------------------------------------------------------------
def log(func):
    def verbose(*args, **kwargs):
        if VERBOSE:
            print(func.__name__, args, kwargs)
        return func(*args, **kwargs)

    return verbose


# ----------------------------------------------------------------------
# CLASSES
# ----------------------------------------------------------------------
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


# ----------------------------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------------------------
@log
def setmode(*args, **kwargs):
    global _mode, _gpio_modes
    _mode = args[0]
    if _mode == BCM:
        _gpio_modes = _gpio_bcm_modes.copy()
    elif _mode == BOARD:
        _gpio_modes = _gpio_board_modes.copy()


@log
def getmode(*args, **kwargs):
    return _mode


@log
def gpio_function(*args, **kwargs):
    return _gpio_modes[args[0]]


@log
def setup(*args, **kwargs):
    if isinstance(args[0], (list, tuple)):
        for c in args[0]:
            setup(c, args[1], **kwargs)
    else:
        _gpio_modes[args[0]] = args[1]
        if "initial" in kwargs:
            _gpio_states[args[0]] = kwargs["initial"]


@log
def output(*args, **kwargs):
    if isinstance(args[0], (list, tuple)):
        if isinstance(args[1], (list, tuple)):
            for c, s in zip(args[0], args[1]):
                output(c, s, **kwargs)
        else:
            for c in args[0]:
                output(c, args[1], **kwargs)
    else:
        _gpio_states[args[0]] = args[1]


@log
def input(*args, **kwargs):
    return _gpio_states[args[0]]


@log
def cleanup(*args, **kwargs):
    global _mode, _gpio_modes
    if len(args) == 0:
        if _mode == BCM:
            _gpio_modes = _gpio_bcm_modes.copy()
        elif _mode == BOARD:
            _gpio_modes = _gpio_board_modes.copy()
    else:
        if isinstance(args[0], (list, tuple)):
            for c in args[0]:
                cleanup(c)
        else:
            if _mode == BCM:
                _gpio_modes[args[0]] = _gpio_bcm_modes[args[0]]
                _gpio_states[args[0]] = _gpio_default_states[args[0]]
            elif _mode == BOARD:
                _gpio_modes[args[0]] = _gpio_board_modes[args[0]]
                _gpio_states[args[0]] = _gpio_default_states[args[0]]


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
