from math import cos, sin
from time import sleep
from tkinter import *

import keyboard
from PIL import ImageTk
from keyboard import *

from renderer.gameState import GameState
from renderer.map import Map
from renderer.player import Player

# Initiation of screen and gamestate
root = Tk()
root.geometry('640x480')
canvas = Canvas(root, width=640, height=480)
canvas.pack(fill=BOTH)

player = Player(30, 30, 1 / 10, 3.14159 / 3)
myMap = Map()
myMap.createMap(10 * 3, 15 * 3, 0.05)
gs = GameState(myMap, player)
oldGs = None
# main loop
monstersRest = gs.monsters.__len__()
print("There are", monstersRest, "monsters. Shut'em all!")
while (1):
    monstersRest = gs.monsters.__len__()
    if(monstersRest==0):
        print("You WON!!!")
        sleep(1)
        sys.exit(0)
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
        player.view += 0.1
    elif is_pressed("a"):
        player.view -= 0.1
    elif is_pressed("SPACE"):
        try:
            gs.monsters.remove(gs.fire())
            print("Killed! Rest:", monstersRest-1)
        except:print ("Dont shoot in my wall!")

    #refresh gamestate
    gs = GameState(myMap, player)

    #if gs not changed, why dont we show same picture again&
    if(oldGs!=gs):
        # rendering
        src = gs.render()
        img = src[1].img
        map = src[0].img
        image = ImageTk.PhotoImage(img)
        map = ImageTk.PhotoImage(map) 

        #removing old images
        for k in canvas.children:
            try:
                k.destroy()
            except:
                pass
        #adding new
        imagesprite = canvas.create_image(320, 240, image=image)
        mapsprite = canvas.create_image(80, 60, image=map)
        canvas.update()
        oldGs = gs
