from OurProgram.RobotClass import *
import time
from SensorsMethods.SensorsDAQ_Slow import get_color
import serial

MyRoboticArm = RoboticArm()

# Pick up positions
# x_value =  -100
# y_value =  200
# z_value =  80
def GoToPickPos(speed):
    x = -100
    y = 200
    z = 280
    MyRoboticArm.GoToXyZ(x, y, z, speed)
    x = -100
    y = 200
    z = 100
    MyRoboticArm.GoToXyZ(x, y, z, speed)
    MyRoboticArm.EndEffector(70, 5000)


# Distination Position 1 - RED
# x = 150
# y = -250
# z = 80
def GoToDstRED(speed):
    x = -100
    y = 200
    z = 200
    MyRoboticArm.GoToXyZ(x, y, z, speed)
    x = 150
    y = -250
    z = 150
    MyRoboticArm.GoToXyZ(x, y, z, speed)
    MyRoboticArm.EndEffector(120, 5000)
    MyRoboticArm.GoToMainHomePosition(5000)


# Distination Position 2
# x = -100
# y = -320
# z = 80
def GoToDstGRN(speed):
    x = -100
    y = 200
    z = 200
    MyRoboticArm.GoToXyZ(x, y, z, speed)
    x = -100
    y = -320
    z = 150
    MyRoboticArm.GoToXyZ(x, y, z, speed)
    MyRoboticArm.EndEffector(120, 5000)
    MyRoboticArm.GoToMainHomePosition(5000)


# Distination positions 3
# x_value =  -50
# y_value =  -200
# z_value =  80
def GoToDstBLUE(speed):
    x = -100
    y = 200
    z = 200
    MyRoboticArm.GoToXyZ(x, y, z, speed)
    x = -50
    y = -200
    z = 150
    MyRoboticArm.GoToXyZ(x, y, z, speed)
    MyRoboticArm.EndEffector(120, 5000)
    MyRoboticArm.GoToMainHomePosition(5000)


def RunEE(angle, speed):
    MyRoboticArm.EndEffector(angle, speed)

i = 0
while True:
    if i == 0:
        MyRoboticArm.GoToMainHomePosition(5000)
        RunEE(120, 5000)
        i = 1
    get_color()
    COLOR, IR = get_color()
    if IR == 0:
        print("IR = ", IR)
        print("COLOR: ", COLOR)
    if IR == 1:
        GoToPickPos(5000)
        print("IR = ", IR)
        print("COLOR: ", COLOR)
        if COLOR == "RED":
            GoToDstRED(5000)
        if COLOR == "GREEN":
            GoToDstGRN(5000)
        if COLOR == "BLUE":
            GoToDstBLUE(5000)