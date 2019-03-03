# Multiple buzzer frequency example(2 at the same time)
import pyb
from pyb import Pin, Timer

buzzer1 = 550
buzzer2 = 550

# set-up pin PWM timer for output to buzzer
p2 = Pin("Y2") #Pin Y2 with timer 8 channel 2
tim = Timer(8, freq = 2000)
ch = tim.channel(2, Timer.PWM, pin = p2)

# set-up pin PWM timer for output to buzzer
p7 = Pin("Y7") #Pin Y7 with timer 12 channel 1
tim2 = Timer(12, freq = 2000)
ch2 = tim.channel(1, Timer.PWM, pin = p7)

tim.freq(buzzer1)
tim2.freq(buzzer2)
ch.pulse_width_percent(40)
ch2.pulse_width_percent(40)
pyb.delay(1000) # Allows the buzzer to sound for a second
ch.pulse_width_percent(0) # Turns off buzzer
ch2.pulse_width_percent(0)
pyb.delay(1000)
