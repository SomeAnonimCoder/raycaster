import math
from random import randint

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
              Color(30, 0, 0)
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


    # Creating random map. Issue is to make this map more
    # comfortable - now it's a lot of separate parts of wall
    def createMap(self, w,h, p):
        map = []
        i = []
        for k in range(1,h+1):
            i.append(1)
        map.append(i)
        for i in range(0,w-2):
            part = []
            for j in range(0,h):
                if(randint(0,100)<100*p):
                    part.append((randint(1,10)))
                else:part.append(0)
            part[0] = randint(1,10)
            part[h-1] = randint(1,10)
            map.append(part)
        i = []
        for k in range(1, h+1):
            i.append(1)
        map.append(i)

        self.mapArr = map
        self.w = w
        self.h = h


    # function returning type of wall or 0 if there's no wall in this coordinates
    # First index is 0!!!
    def get(self, x, y):
        return self.mapArr[math.floor(x)][math.floor(y)]


    #returns true if map is free at this coordinates(Attention, monsters don't count!)
    def empty(self, x, y):
        if 0 == self.mapArr[math.floor(x)][math.floor(y)]:
            return True
        return False
