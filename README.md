# fakeRPiGPIO

This package is used to simulate the
[RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO) module.
This package only contains the functions in the RPi.GPIO package without
the functionality. Useful to debug code outside the RPi.
To avoid printing the callings to the package, set `VERBOSE` to `False`:

```python
from RPi import GPIO
GPIO.VERBOSE = False
more_code()
```

## License
> Python fake RPi.GPIO library
> Copyright (C) 2020 Luiz Eduardo Amaral <luizamaral306@gmail.com>
>
> This program is free software: you can redistribute it and/or modify
> it under the terms of the GNU General Public License as published by
> the Free Software Foundation, either version 3 of the License, or
> (at your option) any later version.
> This program is distributed in the hope that it will be useful,
> but WITHOUT ANY WARRANTY; without even the implied warranty of
> MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
> GNU General Public License for more details.
> You should have received a copy of the GNU General Public License
> along with this program.  If not, see <http://www.gnu.org/licenses/>.
