import serial
import time
from movement_calc import calcMovement
import camera.camera as camera
from threading import Thread

def speed():

    while True:
        x, y = camera.robotCenter

        xg = 30.0
        yg = 40.0
        speedcoef = 255  # 0 no movement - 255 full speed

        global msg
        msg = " ".join(str(v) for v in calcMovement(x, y, xg, yg, speedcoef))
        print(msg)

        time.sleep(1)


def sendserial():
    ser = serial.Serial('COM5', 9600, timeout=0.1)
    ser.flush()
    #print("should send " + msg)
    while True:
        ser.write(str.encode(msg))
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        time.sleep(1)

Thread(target=speed).start()
Thread(target=camera.camera).start()
Thread(target=sendserial).start()
