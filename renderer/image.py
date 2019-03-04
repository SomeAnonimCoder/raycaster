from PIL import Image
from math import sqrt

"""
This is my bicycle wrap for PIL(low)
"""


class Color:
    r = 0
    g = 0
    b = 0

    def __init__(self, r, g, b):
        self.setColor(r, g, b)

    def setColor(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def getColor(self):
        return self.r, self.g, self.b


class Frame:
    img = None
    h = 0
    w = 0


    def __init__(self, w, h, color):
        self.img = Image.new("RGB", (h, w), color.getColor())
        self.h = h
        self.w = w

    def clear(self):
        w = self.w
        h = self.h
        self.img = Image.new("RGB", (h, w), Color.getColor())

    def save(self, name):
        self.img.save(name)

    def setPixel(self, x, y, color):
        try:
            self.img.putpixel((int(x), int(y)), color.getColor())
        except:
            #print(x, y)
            pass

    def drawRectangle(self, x, y, h, w, color):
        for a in range(int(x), int(h)):
            for b in range(int(y), int(w)):
                self.setPixel(a, b, color)

    def drawTexture(self, x, y, h, w, texture,x1,y1, cellW, cellH):
        text = Image.open(texture)
        for i in range(int(x), int(h)):
            for j in range(int(y), int(w)):

                try:
                    color = text.getpixel((
                        int(abs(x1/cellW + y1/cellH - int(x1/cellW+y1/cellH))*text.size[1]),
                        abs(int(text.size[1] / ((y-w)) * (j-w)))
                    ))
                except:
                   color = (0,0,0)


                self.setPixel(i, j, Color(color[0], color[1], color[2]))
    def makeWorld(self):
        self.img = Image.open("renderer/res/background.jpg")


# #Example;
# #creating color and image
# color = Color(50, 150, 50)
# img = Frame(100, 100, color)
# #set random black points
# import random
# color = Color(0, 0, 0)
# img.drawTexture(0, 0, 100, 100, "renderer/res/stone.jpeg", 200, 200, 0.6)
# #saving image
# img.save("test.png")
