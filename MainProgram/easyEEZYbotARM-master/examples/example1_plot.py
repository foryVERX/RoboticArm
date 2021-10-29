# Import EEZYbotARM library
from easyEEZYbotARM.kinematic_model import EEZYbotARM_Mk2
from easyEEZYbotARM.kinematic_model import EEZYbotARM_Mk1

# initial joint angles
jointAngle1 = 0
jointAngle2 = 90
jointAngle3 = -135

# Create an EEZYbotARM Mk2 object
myRobotArm = EEZYbotARM_Mk2(jointAngle1, jointAngle2, jointAngle3)
# Plot it


servoAngle_q1, servoAngle_q2, servoAngle_q3 = myRobotArm.map_kinematicsToServoAngles()
print("Base Servo Angle Q1= ", servoAngle_q1)
print("Main arm Servo Angle Q2= ", servoAngle_q2)
print("Hor arm Servo Angle Q3= ", servoAngle_q1)

myRobotArm.plot()
