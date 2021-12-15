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
    x = -90
    y = 120
    z = 280
    MyRoboticArm.GoToXyZ(x, y, z, speed)
    x = -130
    y = 200
    z = 90
    MyRoboticArm.GoToXyZ(x, y, z, speed)
    MyRoboticArm.EndEffector(80, 5000)


# Distination Position 1 - RED
# x = -100
# y = -350
# z = 80
def GoToDstRED(speed):
    x = -100
    y = 200
    z = 280
    MyRoboticArm.GoToXyZ(x, y, z, speed)
    x = -120
    y = -330
    z = 150
    MyRoboticArm.GoToXyZ(x, y, z, speed)
    MyRoboticArm.EndEffector(130, 5000)
    HomePos(5000)


# Distination Position 2
# x = -100
# y = -320
# z = 80
def GoToDstGRN(speed):
    x = -100
    y = 200
    z = 280
    MyRoboticArm.GoToXyZ(x, y, z, speed)
    x = -90
    y = -290
    z = 150
    MyRoboticArm.GoToXyZ(x, y, z, speed)
    MyRoboticArm.EndEffector(130, 5000)
    HomePos(5000)


# Distination positions 3
# x_value =  -50
# y_value =  -200
# z_value =  80
def GoToDstBLUE(speed):
    x = -100
    y = 200
    z = 280
    MyRoboticArm.GoToXyZ(x, y, z, speed)
    x = -45
    y = -210
    z = 220
    MyRoboticArm.GoToXyZ(x, y, z, speed)
    MyRoboticArm.EndEffector(130, 5000)
    HomePos(5000)


def RunEE(angle, speed):
    MyRoboticArm.EndEffector(angle, speed)

# Almost Home Position x= 190.945, y=0 , z=123.05
def HomePos(speed):
    MyRoboticArm.GoToXyZ(190, 0, 200, speed)
    MyRoboticArm.GoToXyZ(195, 0, 125, speed)

i = 0
while True:
    if i == 0:
        HomePos(5000)
        RunEE(140, 5000)
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