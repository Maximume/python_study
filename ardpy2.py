import serial
import time
import keyboard

ard = serial.Serial('COM5', 115200)

while True:

    cmd = input('cmd : ')
    ard.write(cmd.encode())

    if ard.readable():
        print(ard.readline())