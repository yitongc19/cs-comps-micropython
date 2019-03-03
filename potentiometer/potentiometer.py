# Potentiometer example
# From Github https://github.com/mithru/MicroPython-Examples/blob/master/02.Inputs/potentiometer.py

import pyb
from pyb impor Pin, ADC

pot_pin_adc = pyb.ADC(pyb.Pin.board.X1)

led = pyb.LED(4)

while True:
  # dividing by 16 since .read() gives a 12 bit value
  # but .intensity() needs a 8bit value
  # ensuring pot_values is an integer
  pot_value = int(pot_pin_adc.read / 16)
  led.intensity(pot_value)
  print(pot_value)
  
