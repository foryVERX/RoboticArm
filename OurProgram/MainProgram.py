from OurProgram.RobotClass import *
import time

import serial

ser = serial.Serial('COM4', baudrate=9600, timeout=1)

MyRoboticArm = RoboticArm()


# MyRoboticArm.GoToMainHomePosition(3000)

# Pick up positions
# x_value =  -100
# y_value =  200
# z_value =  80
def GoToPickPos(speed):
    x = -100
    y = 200
    z = 200
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


def get_cs_values():
    time.sleep(2)
    ser.write(b'c')
    # csData = ser.readline().decode('utf').rstrip('\n')
    csData = ""
    csData = ser.readline().decode('ascii')
    return csData


def get_color():
    start = cs_data.find("R") + len("R")
    end = cs_data.find("G")
    red = str(cs_data[start:end])
    start = cs_data.find("G") + len("G")
    end = cs_data.find("B")
    green = str(cs_data[start:end])
    start = cs_data.find("B") + len("B")
    blue = str(cs_data[start:])
    if red > green and red > blue:
        color = "RED"
        return color
    elif green > blue:
        color = "GREEN"
        return color
    else:
        color = "BLUE"
        return color

i = 0
while True:
    if i == 0:
        MyRoboticArm.GoToMainHomePosition(5000)
        RunEE(120, 5000)
        i = 1
    cs_data = get_cs_values()
    print("Color Data", cs_data)
    ser.flushInput()
    ser.flushOutput()
    time.sleep(2)
    if len(cs_data) == 0:
        ir = 0
        MyRoboticArm.GoToMainHomePosition(5000)
    else:
        ir = 1
        color = get_color()
        GoToPickPos(5000)
        print("ir = ", ir)
        print("color is ", color)
        time.sleep(2)
        if color == "RED":
            GoToDstRED(5000)
        if color == "GREEN":
            GoToDstGRN(5000)
        if color == "BLUE":
            GoToDstGRN(5000)


    # if data vailable robotic arm pick
