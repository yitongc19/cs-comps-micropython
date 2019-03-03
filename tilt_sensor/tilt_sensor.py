# Tilt Sensor Example
from pyb import Pin, ADC

tiltSensor = ADC(Pin('X1'))

while True:
  print(tiltSensor.read())
