import copy
from math import *

from renderer.image import *
from renderer.map import *
from renderer.player import Player

# Number of rays casting per image
RAY_NUM = 200

"""
Class containing game status and rendering it
"""


# TODO бросать попеременно четные и нечетные лучи! FPS *2. Спасибо Олегу


class GameState:
    map = []
    player = None
    monsters = []
    mapFB = Frame(100, 150, Color(100, 100, 100))
    screenFB = Frame(480, 640, Color(0, 0, 0))
    screenFB.makeWorld()
    def __init__(self, map: Map, player: Player):
        self.map = map
        self.player = player

    def render(self):
        map = self.map
        player = self.player
        mapFB = copy.deepcopy(self.mapFB)
        screenFB = copy.deepcopy(self.screenFB)

        # Size of one cell on the map
        mapCellW = mapFB.w / (map.w)
        mapCellH  = mapFB.h / map.h

        # size of one cell on the screen
        screenCellW = screenFB.w / map.w
        screenCellH = screenFB.h / map.h

        # drawing walls:
        for i in range(0, map.w):
            for j in range(0, map.h):
                if not map.empty(i, j):
                    mapFB.drawRectangle(j * mapCellH,i * mapCellW,
                                       (j + 1) * mapCellH,   (i + 1) * mapCellW,
                                        Color(0, 0, 0))

        # iterating alpha
        alpha = player.view - player.fov / 2
        mapFB.drawRectangle( player.y - 1, player.x - 1, player.y + 1,player.x + 1, Color(255, 0, 0))
        rayNum = 0
        while alpha < player.fov / 2 + player.view:
            # iterating distance
            dist = 0
            x = player.x
            y = player.y
            while 0 < x < mapFB.w - 1 and 0 < y < mapFB.h - 1:

                # coordinates of current point of ray
                x = dist * cos(alpha) + player.x
                y = dist * sin(alpha) + player.y
                dist += 0.1

                beta = alpha - player.view

                # if we see the point - draw it gray on map
                if map.empty(x / mapCellW, y / mapCellH):
                    mapFB.setPixel(y, x, Color(200, 200, 200))
                else:
                    #drawing Walls
                    if (
                            -1000 / dist*cos(beta) + screenFB.w / 2 > 0 and rayNum * screenCellH > 0 and 1000 / dist*cos(beta) + screenCellW / 2 < screenFB.w and (
                            rayNum + 1) * screenFB.h / RAY_NUM < screenFB.h):

                        screenFB.drawTexture(

                            rayNum * screenFB.h / RAY_NUM,
                            -1000 / dist/cos(beta) + screenFB.w / 2,
                            (rayNum + 1) * screenFB.h / RAY_NUM,
                            1000 / dist/cos(beta) + screenFB.w / 2,
                            "renderer/res/" + str(map.get(x / mapCellW, y / mapCellH)%4+1)+".jpg",
                            x,y,
                            mapCellW, mapCellH
                        )
                    break


            rayNum += 1
            # casting RAY_NUM rays per image
            alpha += player.fov / RAY_NUM

        return mapFB, screenFB
"""
#Example:  save 10 photos of map and screen 
map = Map()
for i in range(0, 10):
    player = Player(30, 20, 0 + i / 10, 3.14159 / 4)
    gs = GameState(map, player)
    screen = gs.render()
    screen[0].save("map" + str(i) + ".jpg")
    screen[1].save("screen" + str(i) + ".jpg")
"""
