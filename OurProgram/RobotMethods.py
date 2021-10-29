# Import EEZYbotARM library
import time

from easyEEZYbotARM.kinematic_model import EEZYbotARM_Mk2
from easyEEZYbotARM.serial_communication import arduinoController

# Insert your Arduino serial port here to initialise the arduino controller
myArduino = arduinoController(port="COM3")
myArduino.openSerialPort()

# Variables
servoAngle_EE_closed = 60
servoAngle_EE_open = 90

# Initializing Servo Angles
servoAngle_q1 = 90
servoAngle_q2 = 90
servoAngle_q3 = 90

# Creating Instance of RoboticArm
myVirtualRobotArm = EEZYbotARM_Mk2(
    initial_q1=0, initial_q2=90, initial_q3=-135)


def GoToMainHomePosition(speed):
    # Initialise kinematic model with initial joint angles (home position)
    # Define end effector open and closed angle
    # Calculate the current servo angles
    servoAngle_q1, servoAngle_q2, servoAngle_q3 = myVirtualRobotArm.map_kinematicsToServoAngles(q1=0,
                                                                                                q2=90,
                                                                                                q3=-135)

    # Send the movement command to the arduino. The physical EEZYbotARM will move to this position
    myArduino.communicate(data=myArduino.composeMessage(servoAngle_q1=servoAngle_q1,
                                                        servoTime1=speed,
                                                        servoAngle_q2=servoAngle_q2,
                                                        servoTime2=speed,
                                                        servoAngle_q3=servoAngle_q3,
                                                        servoTime3=speed,
                                                        servoAngle_EE=servoAngle_EE_open))


def EndEffector(Close_angle, Open_angle, speed):
    # Initialise kinematic model with initial joint angles (home position)
    # Define end effector open and closed angle
    if Close_angle >= 60:
        # Send the movement command to the arduino. The physical EEZYbotARM will move to this position
        myArduino.communicate(data=myArduino.composeMessage(servoAngle_q1=servoAngle_q1,
                                                            servoTime1=speed,
                                                            servoAngle_q2=servoAngle_q2,
                                                            servoTime2=speed,
                                                            servoAngle_q3=servoAngle_q3,
                                                            servoTime3=speed,
                                                            servoAngle_EE=Close_angle,
                                                            servoTime_EE=speed))
    if Open_angle > 60:
        # Send the movement command to the arduino. The physical EEZYbotARM will move to this position
        myArduino.communicate(data=myArduino.composeMessage(servoAngle_q1=servoAngle_q1,
                                                            servoTime1=speed,
                                                            servoAngle_q2=servoAngle_q2,
                                                            servoTime2=speed,
                                                            servoAngle_q3=servoAngle_q3,
                                                            servoTime3=speed,
                                                            servoAngle_EE=Open_angle,
                                                            servoTime_EE=speed))

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


GoToXyZ(-12, -200, 40, 3000)
GoToMainHomePosition(3000)

# Close the serial port
myArduino.closeSerialPort()
