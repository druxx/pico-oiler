# pico-oiler
DIY motorcycle chain oiler

This repository describes a small device to be mounted on a motorcycle triggering emission of oil drops directly onto the drive chain of the motorcycle.

The project is heavily based on ...

The small control unit uses a [Raspberry Pi Pico W](https://www.raspberrypi.com/products/raspberry-pi-pico/) board extended by a GPS module and a mosfet hat to drive a pump.

The firmware for the Pico board is written in [MicroPython](https://micropython.org) for the [Pico W](https://micropython.org/download/RPI_PICO_W/).

Several open source Python packages are used:


* [Microdot](https://microdot.readthedocs.io/en/latest/index.html)
