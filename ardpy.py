import serial
import time
import keyboard

ard = serial.Serial('COM5', 115200)

avg = 0
n = 1
res = []
while True:

    # if keyboard.is_pressed('1'):
    #     ard.write('1'.encode())
    # elif keyboard.is_pressed('0'):
    #     ard.write('0'.encode())

    if ard.readable():
        try:
            distance = float(str(ard.readline())[2:-5])
            # time.sleep(0.01)
            if distance > 450 or distance < 2:
                print("INVALID VALUE!!!")
            else:
                avg = distance if n==1 else (avg * (n-1) + distance) / n
                # if n == 1: avg = distance
                # else: avg = (avg * (n-1) + distance) / n

                n += 1

            if n > 100:
                res.append(round(avg,4))
                n = 1
                avg = 0

        except ValueError:
            pass

        print(res)