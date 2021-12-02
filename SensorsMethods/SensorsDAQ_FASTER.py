import serial
import time

ser = serial.Serial('COM3', baudrate=9600, timeout=1)


def colorSensor():
    arduinoData = ser.readline().decode('ascii')
    ser.flushInput()
    ser.flushOutput()
    cs_data = arduinoData
    #arduinoData = ser.readline()
    print("length of csdata: ", len(cs_data))
    if not len(cs_data) == 0:
        start = cs_data.find("R") + len("R")
        end = cs_data.find("G")
        red = str(cs_data[start:end])
        start = cs_data.find("G") + len("G")
        end = cs_data.find("B")
        green = str(cs_data[start:end])
        start = cs_data.find("B") + len("B")
        blue = str(cs_data[start:])
        if red > green and red > blue:
            color = "RED"
            print("IR SENSOR: 1")
            return color
        elif green > blue:
            color = "GREEN"
            print("IR SENSOR: 1")
            return color
        else:
            color = "BLUE"
            print("IR SENSOR: 1")
            return color
    else:
        print("IR SENSOR: 0")

while True:
    tic = time.perf_counter()
    print("Color Values: ", colorSensor())
    toc = time.perf_counter()
    print(f"Time Taken:   {toc - tic:0.4f} seconds")
