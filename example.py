#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Fake RPi.GPIO example
'''
#______________________________________________________________________
# imports
from RPi import GPIO

#______________________________________________________________________
# globals
channel = 0
frequency = 100
dc = 50

#______________________________________________________________________
# testing functions
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.output(channel, GPIO.HIGH)
print(GPIO.input(channel))
GPIO.wait_for_edge(channel, GPIO.RISING)
GPIO.event_detected(channel)
GPIO.add_event_detect(channel)
GPIO.add_event_callback(channel)
GPIO.remove_event_detect(channel)
GPIO.cleanup()

#______________________________________________________________________
# testing PWM
p = GPIO.PWM(channel, frequency)
p.start(dc)
p.ChangeFrequency(frequency/2)
p.ChangeDutyCycle(dc/2)
p.stop()
