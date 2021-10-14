from time import sleep
from pyfirmata import Arduino, SERVO, util

# Q1 Base from Default Pos is 90 Deg
# Q2 Main Arm Default Pos is 90 Deg
# Q3 Horizental Default Pos is 45 Deg

# EE Open (90 - 60), Close depends on the box width
# Q1 PWM 9
# Q3 PWM 3
# Q2 PWM 6
port = 'COM4'
pin = 9
board = Arduino(port)
board.digital[pin].mode = SERVO
pin9 = board.get_pin('d:9:s')


# First method to move the servo
def rotate_servo(pin, angle):
    board.digital[pin].write(angle)


# Second method to move the servo
def move_servo(angle):
    pin9.write(angle)


rotate_servo(pin, 90)

while True:
    # Reads and handles data from the microcontroller over th-e serial port. This method
    # should be called in a
    # main loop or in an Iterator instance to keep this boards pin values up to date
    iter8 = util.Iterator(board)
    iter8.start()
    sleep(0.15)
    user_angle = input("Choose an angle =  ")
    try:  # To only accept integer values
        int(user_angle)
        its_int = True
    except ValueError:
        its_int = False
    if its_int:
        rotate_servo(pin, user_angle)
        sleep(0.15)
