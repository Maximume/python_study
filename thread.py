import threading
import keyboard
import time

def th1():
    while True:
        print('working...')
        time.sleep(0.1)


def th2():
    while True:
        if keyboard.is_pressed('1'):
            print('pressed 1')
            time.sleep(0.1)

if __name__ == '__main__':
    task1 = threading.Thread(target=th1)
    task2 = threading.Thread(target=th2)

task1.start()
task2.start()
