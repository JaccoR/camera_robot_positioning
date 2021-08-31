import cv2
import util as u

pixelSize = 200

#generates 5 arucocodes, one for the robot and 4 for the corners.
#if new robot is added a new aruco code should be generated here

def markerPath(filename):
    return r"C:\Users\reuli\Documents\Bachelor Assignment\Robot project\python\arucocodes\\" + filename

corner_UL = cv2.aruco.drawMarker(u.dictionary, 23, pixelSize)
cv2.imwrite(markerPath('UL.png'), corner_UL)

corner_UR = cv2.aruco.drawMarker(u.dictionary, 24, pixelSize)
cv2.imwrite(markerPath('UR.png'), corner_UR)

corner_DL = cv2.aruco.drawMarker(u.dictionary, 25, pixelSize)
cv2.imwrite(markerPath('DL.png'), corner_DL)

corner_DR = cv2.aruco.drawMarker(u.dictionary, 26, pixelSize)
cv2.imwrite(markerPath('DR.png'), corner_DR)

robot1 = cv2.aruco.drawMarker(u.dictionary, 30, pixelSize)
cv2.imwrite(markerPath('robot1.png'), robot1)