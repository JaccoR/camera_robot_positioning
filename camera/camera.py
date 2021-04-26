import cv2
import json
import numpy as np
import util as u
from calibration.undistort import undistort
from calibration.transformer import transform
import time

resolution = (960, 720)
cap = cv2.VideoCapture(0)


def camera():
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        dst = undistort(gray)
        warped = transform(gray)
        cv2.imshow("gray", gray)
        cv2.imshow("dst", dst)


        if arucocenterupfind(warped) is not None:
            global robotCenter, robotUp
            robotCenter, robotUp = arucocenterupfind(warped)
            #print(robotCenter)
            cv2.circle(warped, (robotCenter[0], robotCenter[1]), 4, (0, 0, 255), -1)
            cv2.line(warped, tuple(robotCenter), tuple(robotUp), (0, 255, 0), 2)

        cv2.imshow("transform", warped)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

def arucocenterupfind(warped):
    robotCorners, robotId = u.detectAruco(warped)

    robotCenter = [0, 0]
    robotUp = [0, 0]
    if robotId == [30]:
        robotCenter, robotUp = u.centerAndUp(robotCorners)

        return robotCenter, robotUp
