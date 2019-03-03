from pyb import Pin, ADC

#Light sensor example

lightSensor = ADC(Pin('X1'))

while True:
  print(lightSensor.read())
