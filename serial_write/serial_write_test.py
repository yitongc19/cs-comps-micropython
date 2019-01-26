import pyb
import utime

# Connect the buttons and then press 'RST'
# on the board to run the program. Open
# another terminal window to run input_handle.py.

button1 = pyb.Pin('X1', pyb.Pin.IN)
button2 = pyb.Pin('X2', pyb.Pin.IN)
button3 = pyb.Pin('X3', pyb.Pin.IN)
button4 = pyb.Pin('X4', pyb.Pin.IN)

while True:
    if button1.value() == 0:
        print('A')
    elif button2.value() == 0:
        print('B')
    elif button3.value() == 0:
        print('C')
    elif button4.value() == 0:
        print('D')