import serial
import time
from movement_calc import calcMovement
import camera.camera as camera
from threading import Thread

msg = None
def speed():
    while True:
        if camera.robotCenter is not None:
            x, y = camera.robotCenter

            xg = 100.0
            yg = 140.0
            speedcoef = 150  # 0 no movement - 255 full speed

            global msg
            msg = " ".join(str(v) for v in calcMovement(x, y, xg, yg, speedcoef))
            print(msg)

            time.sleep(1)


def sendserial():
    ser = serial.Serial('COM4', 9600, timeout=0.1)
    ser.flush()
    while True:
        if msg is not None:
            ser.write(str.encode(msg))
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            time.sleep(1)


Thread(target=camera.camera).start()
Thread(target=speed).start()
Thread(target=sendserial).start()
