# Taken from Github
# https://github.com/ShahriyarR/Micro-Python-code-samples/blob/master/RGB_led.py

import pyb
from pyb import Pin

#Blinking Singular color LED example

Ledx1 = pyb.Pin('X1', pyb.Pin.OUT_PP, pyb.Pin.PULL_UP)

LEDx1.low()

try:
  while True:
  
    LEDx1.value(False)
    pyb.delay(1000)
  
    LEDx1.value(True)
    pyb.delay(100)
  
  
except:
  LEDx1.value(False)
