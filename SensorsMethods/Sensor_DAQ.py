import serial
import time

ser = serial.Serial('COM4', baudrate=9600, timeout=1)


def getValues():
    ser.write(b'g')
    arduinoData = ser.readline().decode('ascii')
    return arduinoData

def get_ir_data():
    ir_data = []
    for i in range(10):
        time.sleep(0.1)
        value = getValues()
        if value == 0:
            value = 1
        else:
            value = 0
        ir_data.append(value)
    return ir_data[9]

get_ir_data()
