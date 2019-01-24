import pyb 
import utime
import sys

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

default_pulse_width = 1500
class Servo:
    def __init__(self, pin_name, interval, incre):
        self.last_update = utime.ticks_ms()
        self.interval = interval
        self.incre = incre
        self.cur_pulse_width = default_pulse_width
        self.servo_pin = pyb.Pin(pin_name)
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
        self.timer = pyb.Timer(timer_idx, prescaler=83, period=19999)
        self.servo = self.timer.channel(ch_idx, pyb.Timer.PWM, pin=self.servo_pin)
        self.servo.pulse_width(self.cur_pulse_width)
    
    
    def update_speed(self, interval, incre):
        self.interval = interval
        self.incre = incre
        
    def update(self):
        
        current_time = utime.ticks_ms()
#        print(current_time - self.last_update)
        if (utime.ticks_diff(current_time, self.last_update)) >= self.interval:
            self.last_update = utime.ticks_ms()
            self.cur_pulse_width += self.incre
            self.servo.pulse_width(self.cur_pulse_width)
            
        if self.cur_pulse_width >= 2140 or self.cur_pulse_width <= 850:
            self.incre = -self.incre
    
    def change_speed(self, new_incre):
        if self.incre < 0:
            self.incre = -new_incre
        else:
            self.incre = new_incre
        
    def angle(self, a, step):
        target_pulse_width = 1500 + a * 10
        if target_pulse_width >= self.cur_pulse_width:
            while self.cur_pulse_width <= target_pulse_width:
#                print(self.cur_pulse_width)
                self.servo.pulse_width(self.cur_pulse_width)
                pyb.delay(20)
                self.cur_pulse_width += step
        else:
            while self.cur_pulse_width >= target_pulse_width:
#                print(self.cur_pulse_width)
                self.servo.pulse_width(self.cur_pulse_width)
                pyb.delay(20)
                self.cur_pulse_width -= step


                