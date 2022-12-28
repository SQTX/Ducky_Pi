# Ducky_Pi
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python 3.6](https://img.shields.io/badge/python-v3.10-informational)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/SQTX/Ducky_Pi)

## Intro
With this library you can turn your Raspberry Pi Pico into a real
'BAD USB'. With little work, you can get a similar result compared
to a professional tool at a much lower price.

## Install
1. Download **CircuitPython** from the official website
   and install it on your Raspberry Pi Pico.<br>
   [Official CircuitPython webside](https://circuitpython.org/board/raspberry_pi_pico/)
   1. Installation on **Windows**: Drag and drop *CircuitPython* file into the Raspberry Pi memory (RPI-RP2).
   2. Installation on **Mac**: Use below command in `Download` folder:<br>
      `cp -X ./adafruit-circuitpython-raspberry_pi_pico-pl-7.3.3.uf2 /Volumes/RPI-RP2/`<br>
      After that RPI-RP2 should change to CIRCUITPY.
2. Download **Adafruit_CircuitPython_HID** library and put it in `lib` directory.<br>
   [Link to  Adafruit_CircuitPython_HID](https://github.com/adafruit/Adafruit_CircuitPython_HID)
3. If you want to use other keyboard's layouts or alphabets than US
   you must download **Circuitpython_Keyboard_Layouts** by *Neradoc*.
   Drag and drop `libraries` directory and put it into `lib` directory.<br>
   [Link to Circuitpython_Keyboard_Layouts](https://github.com/Neradoc/Circuitpython_Keyboard_Layouts)
4. Download the repository. From downloaded content drag all file
   and drop them into Raspberry Pi memory.
5. *It's time to prepare the payload script.*

## Create script
Before you start writing a script, you should turn edit mode on.
This protects you against unwanted autorun of script on your
private computer.
#### Edit mode
- To turn it on you have to connect pin no. 1 (GP0) with anyone ground (GND).
  You can see the specific pins in the figure below.
  ![Pinout and design files](https://www.raspberrypi.com/documentation/microcontrollers/images/pico-pinout.svg)
  *If you turn edit mode on correctly, LED on your Raspberry Pi will be
  flashing with const frequency.*
#### Script
1. Script should be written in `payload.txt` file.
2. Information about all functions and 'how correct use they'
   you can find in this link:
   [Script documentation](https://github.com/SQTX/Ducky_Pi/blob/main/markdown/SCRIPTDOC.md)

## Reset
To reset the memory, drag and drop the `flash_nuke.uf2` file into the Raspberry Pi memory (RPI-RP2).
You can download the file from [here](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/circuitpython).

## Licence MIT
More information you can find here: [Licence MIT](https://github.com/SQTX/Ducky_Pi/blob/main/markdown/LICENSE.md)


