from OurProgram.RobotClass import *

MyRoboticArm = RoboticArm()
MyRoboticArm.SuddenMovementCorrection()

while True:
    speed = 3000
    x, y, z, EE_Angle, command = input("Enter X Y Z, EE_Angle, command(stop)).split()").split()
    x = int(x)
    y = int(y)
    z = int(z)
    EE_Angle = int(EE_Angle)
    command = str(command)
    MyRoboticArm.GoToXyZ(x, y, z, speed)
    MyRoboticArm.EndEffector(EE_Angle, speed)
    if command == "stop":
        MyRoboticArm.GoToMainHomePosition(speed)
        break
