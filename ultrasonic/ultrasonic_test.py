import pyb
import time
from ultrasonic import Ultrasonic

sensor = Ultrasonic('X1', 'X2')

while True:
    print("Distance in cm: ", sensor.distance_in_cm)
    print("Distance in inches: ", sensor.distance_in_inches)
    time.sleep(10)