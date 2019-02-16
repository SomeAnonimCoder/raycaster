from math import *

from image import *
from map import *
from player import Player

"""
Class containing game status and rendering it
"""


# TODO бросать попеременно четные и нечетные лучи! FPS*2


class GameState:
    map = []
    player = None

    def __init__(self, map: Map, player: Player):
        self.map = map
        self.player = player

    def render(self):
        map = self.map
        player = self.player
        mapFB = Frame(150, 100, Color(255, 255, 255))
        screenFB = Frame(640, 480, Color(255, 255, 255))

        # Size of one cell of map on the screen
        cellW = mapFB.w / map.w
        cellH = mapFB.h / map.h

        # Casting Rays
        i = 0
        while i < mapFB.w / 2:
            angle = player.view - player.fov / 2 + player.fov * i / (mapFB.w / 2);
            j = 0
            while j < 100:
                x = player.x + j * (cos(angle))
                y = player.y + j * (sin(angle))

                # Drawing cone of view
                if (int(x * cellW) < mapFB.w - 1 and int(y * cellH) < mapFB.h - 1):
                    if (not self.map.empty(int(x)/cellW, int(y)/cellH)): mapFB.drawRectangle(x*cellW, y*cellH,(x+1)*cellW, (y+1)*cellH, Color(255,255,255))
                    mapFB.setPixel(int(x * cellW), int(y * cellH), Color(190, 190, 190))
                j += .01


            i += 5
        return mapFB


map = Map()
for i in range(0, 100):
    player = Player(2, 2 + i, 0 + i / 10, 3.14159 / 4)
    gs = GameState(map, player)
    a = gs.render().save
    #a[0].save("map" + str(i) + ".jpg")
    #a[1].save("screen" + str(i) + ".jpg")
