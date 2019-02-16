from math import *

from image import *
from map import *
from player import Player

"""
Class containing game status and rendering it
"""


#TODO бросать попеременно четные и нечетные лучи! FPS *2


class GameState:
    map = []
    player = None

    def __init__(self, map: Map, player: Player):
        self.map = map
        self.player = player

    def render(self):
        map = self.map
        player = self.player
        fb = Frame(150, 100, Color(255, 255, 255))

        # Size of one cell of map on the screen
        cellW = fb.w / map.w
        cellH = fb.h / map.h

        i = 0
        while i < fb.w / 2:
            angle = player.view - player.fov / 2 + player.fov * i / (fb.w / 2);
            j=0
            while j<100:
                x = player.x + j*(cos(angle))
                y = player.y + j*(sin(angle))
                if(int(x * cellW)<fb.w-1 and int(y * cellH)<fb.h-1):
                    if(not self.map.empty(int(x),int(y))):break
                    fb.setPixel(int(x * cellW), int(y * cellH), Color(190, 190, 190))
                j+=.01
            i += 2
        for i in range(0, map.w-1):
            for j in range(0, map.h-1):
                if not map.empty(i,j):
                    fb.drawRectangle(int(i*cellW), int(j*cellH), int((i+1)*cellW), int((j+1)*cellH), Color(0,0,0))
        return fb


map = Map()
for i in range(0,100):
    player = Player(2, 2 + i/10, 0 + i/10, 3.14159 / 4)
    gs = GameState(map, player)
    gs.render().save("map" + str(i) + ".jpg")
