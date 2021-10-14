import serial
import time

ser = serial.Serial('COM4', baudrate=9600, timeout=1)


def get_values():
    ser.write(b'g')
    arduinoData = ser.readline().decode('utf').rstrip('\n')
    return arduinoData


def get_ir_data():
    ir_data = []
    for i in range(10):
        time.sleep(0.1)
        value = get_values()
        value = [int(i) for i in value.split() if i.isdigit()]
        for i in value:
            value = value[0]
        if value == 1:
            value = 0
        else:
            value = 1
        ir_data.append(value)
    return ir_data[9]

print(get_ir_data())

