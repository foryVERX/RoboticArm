# Import EEZYbotARM library
import time

from easyEEZYbotARM.kinematic_model import EEZYbotARM_Mk2
from easyEEZYbotARM.serial_communication import arduinoController

# Insert your Arduino serial port here to initialise the arduino controller
myArduino = arduinoController(port="COM3")
myArduino.openSerialPort()

# Variables
servoAngle_EE_closed = 60
servoAngle_EE_open = 120

# Initializing Servo Angles
servoAngle_q1 = 90
servoAngle_q2 = 90
servoAngle_q3 = 90
servoAngle_EE = 90

# Creating Instance of RoboticArm
myVirtualRobotArm = EEZYbotARM_Mk2(
    initial_q1=0, initial_q2=90, initial_q3=-135)


def GoToMainHomePosition(speed):
    # Initialise kinematic model with initial joint angles (home position)
    # Define end effector open and closed angle
    # Calculate the current servo angles
    #servoAngle_q1, servoAngle_q2, servoAngle_q3 = myVirtualRobotArm.map_kinematicsToServoAngles(q1=0,
                                                                                                #q2=90,
                                                                                                #q3=-135)
    #print("HomePosAngles Q1={} Q2={} Q3={}", servoAngle_q1, servoAngle_q2, servoAngle_q3)
    # Send the movement command to the arduino. The physical EEZYbotARM will move to this position
    myArduino.communicate(data=myArduino.composeMessage(servoAngle_q1=90,
                                                        servoTime1=speed,
                                                        servoAngle_q2=90,
                                                        servoTime2=speed,
                                                        servoAngle_q3=90,
                                                        servoTime3=speed,
                                                        servoAngle_EE=servoAngle_EE))


def EndEffector(angle, speed):
    global servoAngle_EE
    # Initialise kinematic model with initial joint angles (home position)
    # Send the movement command to the arduino. The physical EEZYbotARM will move to this position
    myArduino.communicate(data=myArduino.composeMessage(servoAngle_q1=servoAngle_q1,
                                                        servoTime1=speed,
                                                        servoAngle_q2=servoAngle_q2,
                                                        servoTime2=speed,
                                                        servoAngle_q3=servoAngle_q3,
                                                        servoTime3=speed,
                                                        servoAngle_EE=angle,
                                                        servoTime_EE=speed))
    servoAngle_EE = angle

def GoToXyZ(x, y, z, speed):
    global servoAngle_q1, servoAngle_q2, servoAngle_q3
    # speed measured in degree per sec
    # xyz measured in mm
    # Approximate MainHome Position x=192 y=136 z=122
    # Assign new cartesian position where we want the robot arm end effector to move to
    # (x,y,z in mm from centre of robot base)
    # Compute inverse kinematics
    a1, a2, a3 = myVirtualRobotArm.inverseKinematics(x, y, z)

    # Calculate the current servo angles
    servoAngle_q1, servoAngle_q2, servoAngle_q3 = myVirtualRobotArm.map_kinematicsToServoAngles(q1=a1,
                                                                                                q2=a2,
                                                                                                q3=a3)

    # Send the movement command to the arduino. The physical EEZYbotARM will move to this position
    myArduino.communicate(data=myArduino.composeMessage(servoAngle_q1=servoAngle_q1,
                                                        servoTime1=speed,
                                                        servoAngle_q2=servoAngle_q2,
                                                        servoTime2=speed,
                                                        servoAngle_q3=servoAngle_q3,
                                                        servoTime3=speed))


# Almost Home Position x= 190, y=0 , z=120
# Limit x= 350, y=NA , z=0 .. Y not possible to change
GoToMainHomePosition(0)
GoToXyZ(190, -120, 80, 1000)
GoToMainHomePosition(1000)

# Close the serial port
myArduino.closeSerialPort()
