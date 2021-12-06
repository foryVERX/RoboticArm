from OurProgram.RobotClass import *
import time


MyRoboticArm = RoboticArm()


# EE Open for package is 130
# EE close for package is 63

# Pick up positions
# x_value =  260
# y_value =  -5
# z_value =  55

# Distination positions
# x_value =  -70
# y_value =  -187
# z_value =  118


def GoToPos(x, y, z, speed):
    MyRoboticArm.GoToXyZ(x, y, z, speed)


# Pick up positions
# x_value =  -100
# y_value =  200
# z_value =  80

# Distination Position 1

# x = 150
# y = -250
# z = 80

# Distination Position 2

# x = -100
# y = -320
# z = 80

# Distination positions 3
# x_value =  -50
# y_value =  -200
# z_value =  80


# Almost Home Position x= 190.945, y=0 , z=123.05

i = 0
while True:
    st = time.time()
    MyRoboticArm.GoToMainHomePosition(5000)
    x = int(input("X = "))
    y = int(input("Y = "))
    z = int(input("Z = "))
    speed = 5000
    GoToPos(x,y,z,speed)
    endt = time.time()
    print(f"Runtime of the program is {endt - st}")
