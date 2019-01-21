import pyb
import time
from joystick import Joystick

j = Joystick('X1', 'X2', 'X3')

while True:
    print("status:\n")
    print(j.get_state())
    time.sleep(10)