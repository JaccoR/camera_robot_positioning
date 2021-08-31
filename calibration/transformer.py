import cv2
import numpy as np
import util as u

transformData = u.loadJSON(r"C:\Users\reuli\Documents\Bachelor Assignment\Robot project\python\calibration\transformationMatrix")

#perspective transforms image
def transform(gray):
    warped = cv2.warpPerspective(gray, np.float32(transformData["transform_matrix"]), (transformData["maxWidth"], transformData["maxHeight"]))
    return warped