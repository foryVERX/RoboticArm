import serial
import time

ser = serial.Serial('COM4', baudrate=9600, timeout=1)


# Write c to Arduino, which starts the DAQ for CS sensor.
def get_cs_values():
    input = 'c'
    ser.write(input.encode())
    #time.sleep(0.5)
    arduinoData = ser.readline().decode('ascii')
    ser.flushInput()
    ser.flushOutput()
    #arduinoData = ser.readline()
    return arduinoData



def get_color():
    cs_data = get_cs_values()
    time.sleep(2)
    if cs_data == "":
        ir = 0
        color = "NO READING"
        return color, ir
    else:
        start = cs_data.find("R") + len("R")
        end = cs_data.find("G")
        red = int(cs_data[start:end])
        start = cs_data.find("G") + len("G")
        end = cs_data.find("B")
        green = int(cs_data[start:end])
        start = cs_data.find("B") + len("B")
        blue = int(cs_data[start:])
        ir = 1
        if red > green and red > blue:
            color = "RED"
            return color, ir
        elif green > blue:
            color = "GREEN"
            return color, ir
        else:
            color = "BLUE"
            return color, ir