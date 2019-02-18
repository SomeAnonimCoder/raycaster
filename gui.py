from math import cos, sin
from tkinter import *
from keyboard import *
from time import sleep
from tkinter import *

from PIL import Image as img
from PIL import ImageTk

from renderer.map import Map
from renderer.player import Player
from renderer.render import GameState

root = Tk()
root.geometry('640x480')
canvas = Canvas(root, width=640, height=480)
canvas.pack(fill=BOTH)
player = Player(30, 30, 1 / 10, 3.14159 / 3)
gs = GameState(Map(), player)

while(1):
    oldGs = None
    if is_pressed('w'):
        player.x += cos(player.view)
        player.y += sin(player.view)
    elif is_pressed("s"):
        player.x -= 0.1*cos(player.view)
        player.y -= 0.1*sin(player.view)
    elif is_pressed("d"): player.view+=0.1
    elif is_pressed("a"): player.view -= 0.1
    elif gs == oldGs: continue
    gs = GameState(Map(), player)
    src = gs.render()
    img = src[1].img
    map = src[0].img
    image = ImageTk.PhotoImage(img)
    map = ImageTk.PhotoImage(map)
    for k in canvas.children:
        try:
            k.destroy()
        except:
            pass
    imagesprite = canvas.create_image(320, 240, image=image)
    mapsprite = canvas.create_image(80, 60, image=map)
    canvas.update()
    oldGs = gs
