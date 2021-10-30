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

RunEE(130, 5000)
GoToPickPos(4000)
time.sleep(1)
RunEE(100, 5000)
RunEE(80, 5000)
RunEE(63, 5000)
time.sleep(1)
GoToDstPos(400)
time.sleep(1)
RunEE(80, 5000)
RunEE(130, 5000)
