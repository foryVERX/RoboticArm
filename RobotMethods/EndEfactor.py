from pyfirmata import Arduino, SERVO, util
from time import sleep

port = 'COM4'
pin = 9
board = Arduino(port)
board.digital[pin].mode = SERVO
pin9 = board.get_pin('d:9:s')

# Open the end efactor function
def open_ee(angle):
    pin9.write(angle)

# close the end efactor function
def close_ee(angle):
    pin9.write(angle)


# Open angle is in range 90 - 60
# Close angle is 50
open_ee(90)
sleep(0.15)
close_ee(50)
sleep(2)
open_ee(90)

