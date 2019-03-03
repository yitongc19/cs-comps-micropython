#Little Crash Sensor Example
import pyb
from pyb import Pin, ADC

sw = pyb.Switch()

pin = pyb.Pin('X1', pyb.Pin.IN)

while True:
  #if button is pressed down, 0 is shown
  if pin.value() != True:
    print(0)
    pyb.delay(300)
