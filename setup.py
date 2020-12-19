from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), "r") as f:
    long_description = f.read()

setup(
    name='fakeRPiGPIO',
    version='1.0.0',
    description='fakeRPiGPIO is a package to simulate the RPi.GPIO package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/luxedo/fakeRPiGPIO',
    author='Luiz Eduardo Amaral',
    author_email='luizamaral306@gmail.com',
    license='GPL3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: System :: Hardware',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
    ],
    keywords='RPi fake GPIO',
    packages=['RPi'],
    install_requires=[],

)
