import math

from renderer.image import Color


class Map:
    w = 10
    h = 15
    colors = [Color(0, 0, 0),
              Color(200, 200, 0),
              Color(0, 150, 50),
              Color(120, 100, 120),
              Color(0, 120, 40),
              Color(0,50, 230),
              Color(0, 0, 0),
              Color(0, 40, 0),
              Color(0, 0, 40),
              Color(30, 0, 0),
              ]
    mapArr = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 3, 5, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 9, 8, 1, 5, 1, 4, 6, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
    # Axes: x -->, y - down

    # First index is 0!!!
    def get(self, x, y):
        # +1 for starting \n
        try:return self.colors[self.mapArr[math.floor(x)][math.floor(y)]]
        except:
            print(self.mapArr[math.floor(x)][math.floor(y)])
            return Color(0,0,0)


    def empty(self, x, y):
        if 0 == self.mapArr[math.floor(x)][math.floor(y)]:
            return True
        return False

