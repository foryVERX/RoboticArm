from OurProgram.RobotMethods import *

while True:
    speed = 3000
    SuddenMovementCorrection()
    x, y, z, EE_Angle, command = input("Enter X Y Z, EE_Angle, command(stop)).split()").split()
    GoToXyZ(x, y, z, speed)
    if command == "stop":
        GoToMainHomePosition(speed)
        break
