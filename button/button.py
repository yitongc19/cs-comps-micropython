import pyb
from pyb import Pin, ADC

# Button switche example

sw = pyb.Switch()

pin = pyb.Pin("Y5", pyb.Pin.IN)

while True:
  if pin.value() != True: #When the button is pressed it prints 0 to the screen
    print(0)
    pyb.delay(300)
