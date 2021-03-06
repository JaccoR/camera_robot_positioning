import cv2
import numpy as np
import util as u

#undistort het camerabeeld met de opgeslagen matrix in:
distortionData = u.loadJSON(r"C:\Users\reuli\Documents\Bachelor Assignment\Robot project\python\calibration\calibration")

#undistort het camerabeeld gray
def undistort(gray):
    dst = cv2.undistort(gray, np.float32(distortionData["cameraMatrix"]), np.float32(distortionData["distCoeffs"]),
                        None, np.float32(distortionData["newCameraMatrix"]))

    x, y, w, h = distortionData["validPixROI"]
    dst = dst[y:y + h, x:x + w]
    return dst