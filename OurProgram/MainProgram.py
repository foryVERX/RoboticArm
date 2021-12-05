from OurProgram.RobotClass import *
import time

import serial

ser = serial.Serial('COM3', baudrate=9600, timeout=1)


MyRoboticArm = RoboticArm()
# MyRoboticArm.GoToMainHomePosition(3000)

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


def get_cs_values():
    ser.write(b'c')
    csData = ser.readline().decode('utf').rstrip('\n')
    return csData

while True:
    print("Color Data", get_cs_values())
    # if data vailable robotic arm pick

