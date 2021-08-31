import serial
import time
from movement_calc import calcMovement
import camera.camera as camera
from threading import Thread

msg = None


def speed():
    while True:
        if camera.robotCenter is not None:
            x, y = camera.robotCenter #Haalt xy coordinaten van robot op uit Camera.py

            xg = 100.0 #goalcoordinaten
            yg = 140.0
            speedcoef = 100  # 0 no movement - 255 full speed

            global msg
            msg = " ".join(str(v) for v in calcMovement(x, y, xg, yg, speedcoef)) #maakt de message om te versturen via serial naar de arduino
            print(msg)                                                            #maakt daarbij gebruik van movement_calc.py

            time.sleep(1)

#verstuurt message naar arduino
def sendserial():
    ser = serial.Serial('COM4', 9600, timeout=0.1)
    ser.flush()
    while True:
        if msg is not None:
            ser.write(str.encode(msg))
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            time.sleep(1)

#zorgt er voor dat er 3 functies tegelijk runnen, namelijk camerafeed, movement calculations en de serialverzending
Thread(target=camera.camera).start()
Thread(target=speed).start()
Thread(target=sendserial).start()
