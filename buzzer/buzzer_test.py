import pyb
import time
from buzzer import Buzzer

b1 = Buzzer(1, 50)

b1.play_tone(200, 1000)