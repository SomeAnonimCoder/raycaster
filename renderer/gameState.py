import copy
from math import *

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
            # iterating distance
            dist = 0
            x = player.x
            y = player.y
            while 0 < x < mapFB.w - 1 and 0 < y < mapFB.h - 1:
                if dist>200: break
                # coordinates of current point of ray
                x = dist * cos(alpha) + player.x
                y = dist * sin(alpha) + player.y
                dist += 0.1
                beta = alpha - player.view
                if(dist>=200): break
                # if we see the point - draw it gray on map
                if map.empty(x / mapCellW, y / mapCellH):
                    mapFB.setPixel(y, x, Color(200, 200, 200))
                else:
                    # drawing Walls(not higher than the screen!)
                    if (
                            -1000 / dist * cos(beta) + screenFB.w / 2 > 0 and
                            rayNum * screenCellH > 0 and
                            1000 / dist * cos(beta) + screenCellW / 2 < screenFB.w
                            and (rayNum + 1) * screenFB.h / RAY_NUM < screenFB.h
                    ):
                        screenFB.drawTexture(
                            rayNum * screenFB.h / RAY_NUM, -1000 / dist / cos(beta) + screenFB.w / 2,
                            (rayNum + 1) * screenFB.h / RAY_NUM, 1000 / dist / cos(beta) + screenFB.w / 2,
                            "renderer/res/" + str(map.get(x / mapCellW, y / mapCellH) % 4 + 1) + ".jpg",
                            x, y, mapCellW, mapCellH)
                        break


                #TODO: make better drawing for monster(they should be plane, not cubic as they are now
                if (int(x / mapCellW), int(y / mapCellH)) in self.monsters:
                    # print (int(x / mapCellW), int(y / mapCellH))
                    screenFB.drawTexture(
                        rayNum * screenFB.h / RAY_NUM, -1000 / dist / cos(beta) + screenFB.w / 2,
                        (rayNum + 1) * screenFB.h / RAY_NUM, 1000 / dist / cos(beta) + screenFB.w / 2,
                        "renderer/res/monster.jpg", x, y, mapCellW, mapCellH
                    )
                    break

            rayNum += 1
            # casting RAY_NUM rays per image
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
