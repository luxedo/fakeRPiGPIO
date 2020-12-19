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
import unittest
from RPi import GPIO


class TestRPi_GPIO(unittest.TestCase):
    def test_pwm(self):
        pwm = GPIO.PWM(0, 100)
        pwm.start(10)
        pwm.ChangeFrequency(200)
        pwm.ChangeDutyCycle(20)
        pwm.ChangeDutyCycle(20)
        pwm.stop()

    def test_mode(self):
        GPIO.setmode(GPIO.BCM)
        self.assertEqual(GPIO.getmode(), GPIO.BCM)
        GPIO.setmode(GPIO.BOARD)
        self.assertEqual(GPIO.getmode(), GPIO.BOARD)

    def test_gpio_function(self):
        GPIO.setmode(GPIO.BCM)
        try:
            for i in range(54):
                GPIO.gpio_function(i)
        except:
            self.fail("GPIO.gpio_function raised an inexpected error!")

    def test_setup(self):
        GPIO.setmode(GPIO.BCM)
        try:
            GPIO.setup(0, GPIO.IN)
            GPIO.setup(0, GPIO.OUT)
            GPIO.setup([0, 1, 2], GPIO.I2C)
            GPIO.setup((0, 1, 2), GPIO.SPI)
            GPIO.setup(0, GPIO.OUT, initial=GPIO.HIGH)
            GPIO.setup(0, GPIO.OUT, pull_up_down=GPIO.PUD_UP)
        except:
            self.fail("GPIO.setup raised an inexpected error!")

    def test_output(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(0, GPIO.OUT)
        GPIO.output([0, 1], GPIO.HIGH)
        GPIO.output([0], [GPIO.HIGH])
        GPIO.output((1, 2), (GPIO.LOW, GPIO.HIGH))

    def test_input(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(0, GPIO.IN)
        self.assertNotEqual(GPIO.input(0), None)

    def test_cleanup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(0, GPIO.OUT)
        GPIO.cleanup()
        self.assertEqual(GPIO.gpio_function(0), GPIO.IN)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup([0], GPIO.OUT)
        GPIO.cleanup([0])
        self.assertEqual(GPIO.gpio_function(0), GPIO.IN)
