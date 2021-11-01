from OurProgram.RobotClass import *
import keyboard

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
    x = 260
    y = -5
    z = 55
    MyRoboticArm.GoToXyZ(x, y, z, speed)


def GoToDstPos(speed):
    x = -70
    y = -187
    z = 118
    MyRoboticArm.GoToXyZ(x, y, z, speed)


def RunEE(angle, speed):
    MyRoboticArm.EndEffector(angle, speed)


# Pick up positions
# x_value =  260
# y_value =  -5
# z_value =  55

# Distination positions
# x_value =  -70
# y_value =  -187
# z_value =  118

i = 0
while True:
    if i == 0:
        i += 1
        MyRoboticArm.GoToMainHomePosition(3000)
        #RunEE(130, 3000)
    GoToPickPos(3000)
    RunEE(80, 3000)
    GoToDstPos(2000)
    RunEE(130, 3000)
    GoToPickPos(3000)
