import serial
import time

ser = serial.Serial('COM4', baudrate=9600, timeout=1)


def getValues():
    ser.write(b'g')
    arduinoData = ser.readline().decode('ascii')
    return arduinoData


while (1):

    userInput = 'y'

    if userInput == 'y':
        print(getValues())
        time.sleep(1)
