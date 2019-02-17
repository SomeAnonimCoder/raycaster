from math import *

from renderer.image import *
from renderer.map import *
from renderer.player import Player

# Number of rays casting per image
RAY_NUM = 50

"""
Class containing game status and rendering it
"""


# TODO бросать попеременно четные и нечетные лучи! FPS *2. Спасибо Олегу


class GameState:
    map = []
    player = None

    def __init__(self, map: Map, player: Player):
        self.map = map
        self.player = player

    def render(self):
        map = self.map
        player = self.player
        mapFB = Frame(100, 150, Color(255, 255, 255))
        screenFB = Frame(480, 640, Color(255, 255, 255))

        # Size of one cell on the map
        mapCellW = mapFB.w / map.w
        mapCellH = mapFB.h / map.h

        # size of one cell on the screen
        screenCellW = screenFB.w / map.w
        screenCellH = screenFB.h / map.h

        # drawing walls:
        for i in range(0, map.w):
            for j in range(0, map.h):
                if not map.empty(i, j):
                    mapFB.drawRectangle((i) * mapCellW, (j) * mapCellH, (i + 1) * mapCellW, (j + 1) * mapCellH,
                                        Color(0, 0, 0))

        # iterating alpha
        alpha = player.view - player.fov / 2
        mapFB.drawRectangle(player.x - 1, player.y - 1, player.x + 1, player.y + 1, Color(255, 0, 0))
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
                dist += 0.5
                # if we see the point - draw it gray on map
                if map.empty(x / mapCellW, y / mapCellH):
                    mapFB.setPixel(x, y, Color(200, 200, 200))
                else:
                    if (
                            -1000 / dist + screenFB.w / 2 > 0 and rayNum * screenCellH > 0 and 1000 / dist + screenCellW / 2 < screenFB.w and (
                            rayNum + 1) * screenFB.h / RAY_NUM < screenFB.h):
                        screenFB.drawRectangle(-1000 / dist + screenFB.w / 2, rayNum * screenFB.h / RAY_NUM,
                                               1000 / dist + screenFB.w / 2, (rayNum + 1) * screenFB.h / RAY_NUM,
                                               Color(125, 125, 125));
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