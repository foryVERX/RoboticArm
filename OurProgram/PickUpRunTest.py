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


def GoToPickPos(speed):
    x = 27
    y = 220
    z = 80
    MyRoboticArm.GoToXyZ(x, y, z, speed)
    x = 27
    y = 230
    z = 35
    MyRoboticArm.GoToXyZ(x, y, z, speed)


def GoToDstPos(speed):
    x = -70
    y = -187
    z = 118
    MyRoboticArm.GoToXyZ(x, y, z, speed)


def RunEE(angle, speed):
    MyRoboticArm.EndEffector(angle, speed)


# Pick up positions
# x_value =  227
# y_value =  220
# z_value =  35

# Distination positions 1
# x_value =  -70
# y_value =  -187
# z_value =  118

# Distination Position 2

i = 0
while True:
    st = time.time()
    if i == 0:
        i += 1
        MyRoboticArm.GoToMainHomePosition(3000)
        #RunEE(130, 3000)
    GoToPickPos(3000)
    RunEE(70, 3000)
    GoToDstPos(2000)
    RunEE(130, 3000)
    GoToPickPos(3000)
    endt = time.time()
    print(f"Runtime of the program is {endt - st}")
