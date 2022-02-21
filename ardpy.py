import serial
import time
import keyboard

ard = serial.Serial('COM5', 115200)

while True:

    if keyboard.is_pressed('1'):
        ard.write('1'.encode())
    elif keyboard.is_pressed('0'):
        ard.write('0'.encode())

    if ard.readable():
        print(ard.readline())