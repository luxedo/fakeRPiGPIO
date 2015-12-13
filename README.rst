fakeRPiGPIO
===========

This package is used to simulate the
`RPi.GPIO <https://pypi.python.org/pypi/RPi.GPIO>`__ module. This
package only contains the functions in the RPi.GPIO package without the
functionality. Useful to debug code outside the RPi. To avoid printing
the callings to the package, set ``VERBOSE`` to ``False``:

.. code:: python

    from RPi import GPIO
    GPIO.VERBOSE = False
    more_code()
