import time
import json
import argparse
from datetime import datetime
import math
import cv2
import numpy as np
import util as u
from calibration.undistort import undistort


def order_points(pts):
    pts = np.squeeze(pts)
    # initialzie a list of coordinates that will be ordered
    # such that the first entry in the list is the top-left,
    # the second entry is the top-right, the third is the
    # bottom-right, and the fourth is the bottom-left
    rect = np.zeros((4, 2), dtype="float32")
    # the top-left point will have the smallest sum, whereas
    # the bottom-right point will have the largest sum
    s = np.sum(pts, axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    # now, compute the difference between the points, the
    # top-right point will have the smallest difference,
    # whereas the bottom-left will have the largest difference
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    # return the ordered coordinates
    return rect


def four_point_transform(upLeft, upRight, downLeft, downRight):
    rect = [upLeft, upRight, downRight, downLeft]
    # obtain a consistent order of the points and unpack them
    # individually
    # compute the width of the new image, which will be the
    # maximum distance between bottom-right and bottom-left
    # x-coordiates or the top-right and top-left x-coordinates
    widthA = np.sqrt(((downRight[0] - downLeft[0]) ** 2) + ((downRight[1] - downLeft[1]) ** 2))
    widthB = np.sqrt(((upRight[0] - upLeft[0]) ** 2) + ((upRight[1] - upLeft[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))
    # compute the height of the new image, which will be the
    # maximum distance between the top-right and bottom-right
    # y-coordinates or the top-left and bottom-left y-coordinates
    heightA = np.sqrt(((upRight[0] - downRight[0]) ** 2) + ((upRight[1] - downRight[1]) ** 2))
    heightB = np.sqrt(((upLeft[0] - downLeft[0]) ** 2) + ((upLeft[1] - downLeft[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))
    # now that we have the dimensions of the new image, construct
    # the set of destination points to obtain a "birds eye view",
    # (i.e. top-down view) of the image, again specifying points
    # in the top-left, top-right, bottom-right, and bottom-left
    # order
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")
    # compute the perspective transform matrix and then apply it
    M = cv2.getPerspectiveTransform(np.float32(rect), dst)
    return M, maxWidth, maxHeight

perspectiveTransform = None

cap = cv2.VideoCapture(0)  # video capture source camera (Here webcam of laptop)
ret, frame = cap.read()  # return a single frame in variable `frame`
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

while (True):
    cv2.imshow('img1', gray)  # display the captured image
    if cv2.waitKey(1) & 0xFF == ord('y'):  # save on pressing 'y'
        cv2.imwrite('images/c1.png', gray)
        cv2.destroyAllWindows()
        break

cap.release()
undist = undistort(gray)

markerCorners, markerIds = u.detectAruco(undist)

upLeft = None
upRight = None
downLeft = None
downRight = None

if len(markerIds) == 4:
    upLeft = markerCorners[int(np.where(markerIds == [23])[0])]
    upRight = markerCorners[int(np.where(markerIds == [24])[0])]
    downLeft = markerCorners[int(np.where(markerIds == [25])[0])]
    downRight = markerCorners[int(np.where(markerIds == [26])[0])]

    upLeftCorner = order_points(upLeft)[2]
    upRightCorner = order_points(upRight)[3]
    downLeftCorner = order_points(downLeft)[1]
    downRightCorner = order_points(downRight)[0]

    transform_matrix, maxWidth, maxHeight = four_point_transform(upLeftCorner, upRightCorner, downLeftCorner, downRightCorner)
    print(transform_matrix)
    u.saveJSON(r"C:\Users\reuli\Documents\Bachelor Assignment\Robot project\python\calibration\transformationMatrix",
               dict(transform_matrix=transform_matrix.tolist(), maxWidth=maxWidth, maxHeight=maxHeight))

else:
    print("Not all ArUco codes where found!")
    print(markerIds)
