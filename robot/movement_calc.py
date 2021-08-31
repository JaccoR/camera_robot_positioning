import math

#berkent de snelheid van de motoren aan de hand van x y en x y goal coordinaten
def calcMovement(x, y, xg, yg, speedcoef):
    xdir = (xg - x)
    ydir = (yg - y)
    xunit = xdir / (math.sqrt(xdir ** 2 + ydir ** 2))
    yunit = ydir / (math.sqrt(xdir ** 2 + ydir ** 2))

    V1 = speedcoef * xunit
    V2 = speedcoef * (-xunit * math.cos(math.pi / 3) + yunit * math.sin(math.pi / 3))
    V3 = speedcoef * (-xunit * math.cos(math.pi / 3) - yunit * math.sin(math.pi / 3))

    return round(V1), round(V2), round(V3)
