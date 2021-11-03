import serial
import time

ser = serial.Serial('COM3', baudrate=9600, timeout=1)


# Write g to Arduino, which starts the DAQ for IR sensor.
def get_ir_values():
    ser.write(b'g')
    arduinoData = ser.readline().decode('utf').rstrip('\n')
    return arduinoData


# Write c to Arduino, which starts the DAQ for CS sensor.
def get_cs_values():
    ser.write(b'c')
    arduinoData = ser.readline().decode('utf').rstrip('\n')
    return arduinoData


# Adjust the IR output and output last reading.
# samples is how many times the sensor is read.
# delay is the time between each sample
# best samples value found to be 10
# Only last sample is returned
def get_ir_output(samples, delay):
    ir_output = []
    for i in range(samples):
        time.sleep(delay)
        value = get_ir_values()
        value = [int(i) for i in value.split() if i.isdigit()]
        for i in value:
            value = value[0]
        if value == 1:
            value = 0
        else:
            value = 1
        ir_output.append(value)
    return ir_output[samples - 1]


# Extract raw data out of serial.
# samples is best set to 3 to function fast
# Each sample takes 500 ms approximately.
# Only last sample is returned
def get_cs_output(samples):
    cs_output_raw = []
    for i in range(samples):
        value = get_cs_values()
        cs_output_raw.append(value)
    return cs_output_raw[samples - 1]


# Filter the data received and extract each color.
# Call this function to identify color.
# samples is how many samples is taken from sensor.
# Only last sample is returned.
# Best value of samples found to be 3
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
    print(get_cs_output(3))

# ser.close()
