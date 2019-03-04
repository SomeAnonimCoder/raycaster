from PIL import ImageTk
from math import cos, sin, tan
from tkinter import *

import keyboard
from keyboard import *
from renderer.map import Map
from renderer.player import Player
from renderer.render import GameState





root = Tk()
root.geometry('640x480')
canvas = Canvas(root, width=640, height=480)
canvas.pack(fill=BOTH)
player = Player(30, 30, 1 / 10, 3.14159 / 3)
myMap = Map()
myMap.createMap(10 * 3, 15 * 3, 0.05)
gs = GameState(myMap, player)
oldGs = None

while (1):
    # moving or exiting if some keys pressed
    if is_pressed(keyboard.is_pressed("ESC")):
        sys.exit(-1)
    if is_pressed('w'):
        player.x += 2 * cos(player.view)
        player.y += 2 * sin(player.view)
    elif is_pressed("s"):
        player.x -= 2 * cos(player.view)
        player.y -= 2 * sin(player.view)
    elif is_pressed("d"):
        player.view += 0.3
    elif is_pressed("a"):
        player.view -= 0.3
    elif is_pressed("SPACE"):
        print (gs.fire())
        if(gs.fire()!=None): gs.monsters.remove(gs.fire())
    gs = GameState(myMap, player)
    if(oldGs!=gs):

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
