##
#  Buzzer library adapted from https://github.com/dhylands/upy-rtttl/blob/master/pyb_test.py.
##

from time import sleep_us
from machine import Pin, time_pulse_us

# Define the set of timers 
timer2 = ['X6', 'Y9', 'Y10']
timer4 = ['X9', 'X10', 'Y3', 'Y4']
timer5 = ['X1', 'X2', 'X3', 'X4']
timer8 = ['Y1', 'Y2']
timer12 = ['Y7', 'Y8']
timer13 = ['X7']
timer14 = ['X8']

# Define the set of channels
ch1 = ['X8', 'X7', 'X6', 'X1', 'Y1', 'Y7', 'X9']
ch2 = ['X2', 'Y2', 'Y8', 'X10']
ch3 = ['Y9', 'X3', 'Y3']
ch4 = ['Y10', 'X4', 'Y4']

class Buzzer:
    def __init__(self, pin_name, volume):
        """Volume should be an integer between 0 and 100"""
        if pin_name in timer2:
            timer_idx = 2
        elif pin_name in timer4:
            timer_idx = 4
        elif pin_name in timer5:
            timer_idx = 5
        elif pin_name in timer8:
            timer_idx = 8
        elif pin_name in timer12:
            timer_idx = 12
        elif pin_name in timer13:
            timer_idx = 13
        elif pin_name in timer14:
            timer_idx = 14
        else:
            print("Pin number not supported")
            sys.exit()
        if pin_name in ch1:
            ch_idx = 1
        elif pin_name in ch2:
            ch_idx = 2
        elif pin_name in ch3:
            ch_idx = 3
        elif pin_name in ch4:
            ch_idx = 4
        else:
            print("Pin number not supported")
            sys.exit()
        self.buzzer_timer = pyb.Timer(timer_idx, freq=440)
        self.buzzer_ch = self.buzzer_timer.channel(ch_idx, pyb.Timer.PWM, pin=pyb.Pin.board.BUZZER, pulse_width=0)
        self.pwm = volume

    def play_tone(freq, msec):
        if freq > 0:
            self.buzzer_timer.freq(freq)
            self.buzzer_ch.pulse_width_percent(self.pwm)
            pyb.delay(int(msce *0.9))
            self.buzzer_ch.pulse_width_percent(0)
            pyb.delay(int(msec * 0.1))
            
