import math

class Player:
    #coordinates
    x=0
    y=0

    #view direction and field of view(Radians!!!)
    view = 0
    fov = math.pi/3

    turn =0
    walk=0

    def __init__(self, x, y, v, fov):
        self.x = x
        self.y = y
        self.view = v
        self.fov = fov