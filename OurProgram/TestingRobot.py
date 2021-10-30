from OurProgram.RobotClass import *
import keyboard

MyRoboticArm = RoboticArm()

runCount = 0
x_value = 190
y_value = 0
z_value = 120
ee_value = 130
speed = 4000

def RunXYZ(x, y, z):
    speed = 5000
    x = int(x)
    y = int(y)
    z = int(z)
    MyRoboticArm.GoToXyZ(x, y, z, speed)


def RunEE(angle, speed):
    MyRoboticArm.EndEffector(angle, speed)


def on_press_reaction(event):
    global x_value, y_value, z_value, ee_value, speed
    if event.name == 'q':
        x_value += 1
    if event.name == 'w':
        y_value += 1
    if event.name == 'e':
        z_value += 1
    if event.name == 'a':
        x_value -= 1
    if event.name == 's':
        y_value -= 1
    if event.name == 'd':
        z_value -= 1
    if event.name == 'enter':
        RunXYZ(x_value, y_value, z_value)
        print("\n Robotic Arm Moving")
    if event.name == 'o':
        ee_value = 130
        speed = 4000
        RunEE(ee_value, speed)
    if event.name == 'c':
        ee_value = 63
        speed = 6000
        RunEE(ee_value, speed)
    if event.name == '-':
        MyRoboticArm.GoToMainHomePosition(speed)
        exit()

    print("\n\nx_value = ", x_value)
    print("y_value = ", y_value)
    print("z_value = ", z_value)
    print("ee_value = ", ee_value)

# Pick up positions
# x_value =  260
# y_value =  -5
# z_value =  55

# Distination positions
# x_value =  -70
# y_value =  -187
# z_value =  118

keyboard.on_press(on_press_reaction)

while True:
    if runCount == 0:
        MyRoboticArm.SuddenMovementCorrection()
        runCount += 1
    pass
