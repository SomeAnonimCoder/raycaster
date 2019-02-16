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






map = Map()
for i in range(0,100):
    player = Player(2, 2, 0 + i/10, 3.14159 / 4)
    gs = GameState(map, player)
    gs.render().save("map" + str(i) + ".jpg")
