import math

#
class Player:
    # coordinates
    x = 0
    y = 0

    # view direction and field of view(Radians!!!)
    view = 0
    fov = math.pi / 2

    def __init__(self, y, x, v, fov):
        self.x = x
        self.y = y
        self.view = v
        self.fov = fov
