# Import EEZYbotARM library
import time

from easyEEZYbotARM.kinematic_model import EEZYbotARM_Mk2
from easyEEZYbotARM.serial_communication import arduinoController


# Insert your Arduino serial port here to initialise the arduino controller
class RoboticArm:
    myArduino = arduinoController(port="COM3")
    myArduino.openSerialPort()

    def __init__(self):
        # Initializing Servo Angles
        self.servoAngle_q1 = 90
        self.servoAngle_q2 = 90
        self.servoAngle_q3 = 90
        self.Last_servoAngle_EE = 130  # Default Open Value

        # Save Servo angles
        self.last_servoAngle_q1 = 90
        self.last_servoAngle_q2 = 90
        self.last_servoAngle_q3 = 90

        # Creating Instance of RoboticArm
        self.myVirtualRobotArm = EEZYbotARM_Mk2(
            initial_q1=0, initial_q2=90, initial_q3=-135)

    def closeSerialPort(self):
        self.myArduino.closeSerialPort()

    def GoToMainHomePosition(self, speed):
        # Initialise kinematic model with initial joint angles (home position)
        # Define end effector open and closed angle
        # Calculate the current servo angles
        # servoAngle_q1, servoAngle_q2, servoAngle_q3 = myVirtualRobotArm.map_kinematicsToServoAngles(q1=0,
        # q2=90,
        # q3=-135)
        # print("HomePosAngles Q1={} Q2={} Q3={}", servoAngle_q1, servoAngle_q2, servoAngle_q3)
        # Send the movement command to the arduino. The physical EEZYbotARM will move to this position
        self.myArduino.communicate(data=self.myArduino.composeMessage(servoAngle_q1=90,
                                                                      servoTime1=speed,
                                                                      servoAngle_q2=90,
                                                                      servoTime2=speed,
                                                                      servoAngle_q3=90,
                                                                      servoTime3=speed,
                                                                      servoAngle_EE=self.Last_servoAngle_EE))

    def EndEffector(self, angle, speed):
        # Initialise kinematic model with initial joint angles (home position)
        # Send the movement command to the arduino. The physical EEZYbotARM will move to this position
        if angle > 140:
            self.GoToMainHomePosition(3000)
            raise ValueError('End Effector cannot accept angle > 140 if so will full open the gears')
        else:
            self.myArduino.communicate(data=self.myArduino.composeMessage(servoAngle_q1=self.last_servoAngle_q1,
                                                                          servoTime1=speed,
                                                                          servoAngle_q2=self.last_servoAngle_q2,
                                                                          servoTime2=speed,
                                                                          servoAngle_q3=self.last_servoAngle_q3,
                                                                          servoTime3=speed,
                                                                          servoAngle_EE=angle,
                                                                          servoTime_EE=speed))
        # Save the angle value
        self.Last_servoAngle_EE = angle

    def GoToXyZ(self, x, y, z, speed):
        # speed measured in degree per sec
        # xyz measured in mm
        # Approximate MainHome Position x=192 y=136 z=122
        # Assign new cartesian position where we want the robot arm end effector to move to
        # (x,y,z in mm from centre of robot base)
        # Compute inverse kinematics

        a1, a2, a3 = self.myVirtualRobotArm.inverseKinematics(x, y, z)

        st = time.time()
        # Calculate the current servo angles
        self.servoAngle_q1, self.servoAngle_q2, self.servoAngle_q3 = self.myVirtualRobotArm.map_kinematicsToServoAngles(
            q1=a1,
            q2=a2,
            q3=a3)



        # Send the movement command to the arduino. The physical EEZYbotARM will move to this position
        self.myArduino.communicate(data=self.myArduino.composeMessage(servoAngle_q1=self.servoAngle_q1,
                                                                      servoTime1=speed,
                                                                      servoAngle_q2=self.servoAngle_q2,
                                                                      servoTime2=speed,
                                                                      servoAngle_q3=self.servoAngle_q3,
                                                                      servoTime3=speed,
                                                                      servoAngle_EE=self.Last_servoAngle_EE,
                                                                      servoTimeEE=speed))
        endt = time.time()
        print(f"Runtime of the inverseKinematics By Yousef is {endt - st}\n")
        self.last_servoAngle_q1 = self.servoAngle_q1
        self.last_servoAngle_q2 = self.servoAngle_q2
        self.last_servoAngle_q3 = self.servoAngle_q3


    def SuddenMovementCorrection(self):
        # This function is called at the start of the first robot command to solve sudden move.
        self.GoToMainHomePosition(250)

    # Almost Home Position x= 190.945, y=0 , z=123.05
    # Limit x= 350, y=NA , z=0 .. Y not possible to change

    # Close the serial port
