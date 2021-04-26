import json
import cv2
import numpy as np

dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_50)
detectorParams = cv2.aruco.DetectorParameters_create()
#detectorParams.doCornerRefinement = True
#detectorParams.cornerRefinementMaxIterations = 500
# detectorParams.cornerRefinementWinSize = 1
#detectorParams.cornerRefinementMinAccuracy = 0.001
# detectorParams.minMarkerPerimeterRate = 0.05
# detectorParams.maxMarkerPerimeterRate = 0.2
#detectorParams.adaptiveThreshWinSizeMin = 10
# detectorParams.adaptiveThreshWinSizeStep = 3
#detectorParams.adaptiveThreshWinSizeMax = 10


def saveJSON(filename, data):
  print('Saving to file:', filename)
  out = json.dumps(data)
  with open(filename, 'w') as f:
    f.write(out)

def loadJSON(filename):
  print('Loading from file:', filename)
  with open(filename, 'r') as f:
    data = json.loads(f.read())
    return data

def detectAruco(gray):
  markerCorners, markerIds, rejected = cv2.aruco.detectMarkers(gray, dictionary)
  return markerCorners, markerIds

def centerAndUp(corners):
  corners = np.squeeze(corners)
  center = (corners[0] + corners[1] + corners[2] + corners[3]) / 4.0
  up = (corners[0] + corners[1]) / 2.0

  return center, up