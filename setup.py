from setuptools import setup

setup(
    name='fakeRPiGPIO',
    version='0.3a0',
    description='fakeRPiGPIO is a package to simulate the RPi.GPIO package',
    long_description=open('README.rst').read(),
    url='https://github.com/ArmlessJohn404/fakeRPiGPIO',
    author='Luiz Eduardo Nishino Gomes do Amaral',
    author_email='luizamaral306@gmail.com',
    license='GPL3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: System :: Hardware',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='RPi fake GPIO',
    packages=['RPi'],
    install_requires=[],

)
