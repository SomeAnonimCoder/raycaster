import copy
from math import sqrt, tan

from math import sin, cos

from renderer.image import *
# Number of rays casting per image
from renderer.map import *
from renderer.player import Player

RAY_NUM = 100
#
# """
# Class containing game status and rendering it
# """


class GameState:
    map = []
    player = None
    monsters = [
        (3,3),
        (2,10),
        (6,12),
        (20,10),
                ]
    mapFB = Frame(100, 150, Color(100, 100, 100))
    screenFB = Frame(480, 640, Color(0, 0, 0))
    screenFB.makeWorld()

    def __init__(self, map: Map, player: Player):
        self.map = map
        self.player = player


    # returns None if there no monsters in
    # view ray or coordinates of monster in view ray
    def fire(self):
        map = self.map
        player = self.player
        mapFB = copy.deepcopy(self.mapFB)
        screenFB = copy.deepcopy(self.screenFB)

        # Size of one cell on the map
        mapCellW = mapFB.w / (map.w)
        mapCellH = mapFB.h / map.h
        # iterating alpha
        alpha = player.view

        dist = 0
        x = player.x
        y = player.y
        while 0 < x < mapFB.w - 1 and 0 < y < mapFB.h - 1:

            # coordinates of current point of ray
            x = dist * cos(alpha) + player.x
            y = dist * sin(alpha) + player.y
            dist += 0.1
            beta = alpha - player.view
            if (int(x / mapCellW), int(y / mapCellH)) in self.monsters:
                return (int(x / mapCellW), int(y / mapCellH))

            if map.empty(x / mapCellW, y / mapCellH):
                continue
            if map.get(x / mapCellW, y / mapCellH)!=0:
                return None

    # draw walls on map
    def drawWallsOnMap(self, mapFB):
        map = self.map
        mapCellW = mapFB.w / (map.w)
        mapCellH = mapFB.h / map.h
        for i in range(0, map.w):
            for j in range(0, map.h):
                if not map.empty(i, j):
                    mapFB.drawRectangle(j * mapCellH, i * mapCellW, (j + 1) * mapCellH, (i + 1) * mapCellW,
                                        Color(0, 0, 0))

    #TODO: refactor to more functions with less size

    # draw walls and monsters on screen
    def drawScreen(self, mapFB, screenFB):
        map = self.map
        player = self.player

        mapCellW = mapFB.w / (map.w)
        mapCellH = mapFB.h / map.h

        # size of one cell on the screen
        screenCellW = screenFB.w / map.w
        screenCellH = screenFB.h / map.h

        # iterating alpha
        alpha = player.view - player.fov / 2
        mapFB.drawRectangle(player.y - 1, player.x - 1, player.y + 1, player.x + 1, Color(255, 0, 0))
        rayNum = 0
        while alpha < player.fov / 2 + player.view:
            beta = alpha - player.view
            k = tan(alpha)
            if k == 0: k = 0.0001
            b = player.y - k*player.x
            t = cos(alpha)
            for i in range(0, map.w):
                for j in range(0, map.h):
                    d=-1
                    x=-1
                    y=-1
                    if not map.empty(i, j):
                        x0 = i*mapCellW
                        y0 = j*mapCellH
                        x = (i+1)*mapCellW
                        y = (j+1)*mapCellH

                        y1 = y0;
                        x1 = (y0-b)/k
                        d1 = sqrt(y1**2 + x1**2)
                        if(player.y-y1)/t>0: d1 = 10**3

                        y2 = y
                        x2 = (y1-b)/k
                        d2 = sqrt(y2**2 + x2**2)
                        if(player.y - y2)/t>0:d2 = 10**3

                        y3 = k*x0 + b
                        x3 = x0
                        d3 = sqrt(y3**2 + x3**2)
                        if(player.y - y3)/t>0:d3 = 10**3


                        y4 = k*x1 + b
                        x4 = x
                        d4 = sqrt(y4**2 + x4**2)
                        if(player.y - y3)/t>0:d3 = 10**3


                        dist = min(d1,d2,d3,d4)


                        if dist==d1:x, y = x1,y1
                        elif dist==d2: x,y = x2,y2
                        elif dist==d3: x,y = x3, y3
                        elif dist==d4:x,y = x4, y4

            # drawing Walls(not higher than the screen!)
            screenFB.drawTexture(
                        rayNum * screenFB.h / RAY_NUM, -10000 / dist / cos(beta) + screenFB.w / 2,
                        (rayNum + 1) * screenFB.h / RAY_NUM, 10000 / dist + screenFB.w / 2,
                        "renderer/res/" + str(map.get(i, j) % 4 + 1) + ".jpg",
                         x, y, mapCellW, mapCellH)


            rayNum+=1
            alpha += player.fov / RAY_NUM

            # draw a red point to see where you`ll fire
            screenFB.drawRectangle(screenFB.h/2-5, screenFB.w/2-5,screenFB.h/2+5, screenFB.w/2+5, Color(255,0,0))


    # returns two images. First - image to show as what player see, second -
    # map to show in a corner of screen
    def render(self):
        mapFB = copy.deepcopy(self.mapFB)
        screenFB = copy.deepcopy(self.screenFB)

        # drawing walls:
        self.drawWallsOnMap(mapFB)

        #drawing screen image
        self.drawScreen(mapFB,screenFB)

        return mapFB, screenFB
