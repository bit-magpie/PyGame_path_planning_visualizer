import serial
import time

ser = serial.Serial('/dev/ttyACM0',115200)
while 1:
    ser.write('d')
    print(ser.readline())
    time.sleep(0.5)
