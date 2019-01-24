import pyb
import time
from servo import Servo

s1 = Servo('X1', 20, 10)

# Sweeping 
while True:
    s1.update()