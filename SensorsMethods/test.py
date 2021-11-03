import serial
import time

ser = serial.Serial('COM3', baudrate=9600, timeout=1)

# Write g to Arduino, which starts the DAQ for IR sensor.
def get_ir_values():
    # 2 sec
    input = 'g'
    ser.write(input.encode())
    time.sleep(0.2)
    tic = time.perf_counter()
    arduinoData = ser.readline().decode('ascii')
    # To improve the delay avoid using readline multiple times
    toc = time.perf_counter()
    print(f"Time Taken:   {toc - tic:0.4f} seconds")
    ser.flushInput()
    ser.flushOutput()
    #arduinoData = ser.readline()
    return arduinoData

def get_ir_output(samples, delay):
    ir_output = []

    for i in range(samples):
        time.sleep(delay)
        value = get_ir_values()  # 2 sec
        value = 1 - int(value)  # invert the value
        ir_output.append(value)
    return ir_output[samples - 1]


# Write c to Arduino, which starts the DAQ for CS sensor.
def get_cs_values():
    input = 'c'
    ser.write(input.encode())
    time.sleep(0.7)
    arduinoData = ser.readline().decode('ascii')
    ser.flushInput()
    ser.flushOutput()
    #arduinoData = ser.readline()
    return arduinoData


def get_cs_output(samples):
    cs_output_raw = []
    for i in range(samples):
        value = get_cs_values().strip()
        if not value == "":
            cs_output_raw.append(value)
    return cs_output_raw[samples - 2]
    #return cs_output_raw, len(cs_output_raw)


def filter_colors(samples):
    cs_data = get_cs_output(samples)
    start = cs_data.find("R") + len("R")
    end = cs_data.find("G")
    red = int(cs_data[start:end])
    start = cs_data.find("G") + len("G")
    end = cs_data.find("B")
    green = int(cs_data[start:end])
    start = cs_data.find("B") + len("B")
    blue = int(cs_data[start:])
    if red > green and red > blue:
        color = "RED"
        return color
    elif green > blue:
        color = "GREEN"
        return color
    else:
        color = "BLUE"
        return color


while True:
    #print(filter_colors(3))
    print(filter_colors(3))
    print(get_ir_output(3, 0))


