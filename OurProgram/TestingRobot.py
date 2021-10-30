from OurProgram.RobotMethods import *

while True:
    speed = 3000
    SuddenMovementCorrection()
    x, y, z, EE_Angle, command = input("Enter X Y Z, EE_Angle, command(stop)).split()").split()
    x = int(x)
    y = int(y)
    z = int(z)
    EE_Angle = int(EE_Angle)
    command = str(command)
    GoToXyZ(x, y, z, speed)
    EndEffector(EE_Angle, speed)
    if command == "stop":
        GoToMainHomePosition(speed)
        break
