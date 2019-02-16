from PIL import Image

"""
This is my bicycle wrap for PIL(low)
"""

class Color():
    r = 0;
    g = 0;
    b = 0;

    def __init__(self, r, g, b):
        self.setColor(r, g, b)

    def setColor(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def getColor(self):
        return (self.r, self.g, self.b)


class Frame():
    img = None
    h = 0
    w = 0

    def __init__(self, h, w, color):
        self.img = Image.new("RGB", (h, w), color.getColor())
        self.img.save("test.png")
        self.h = h
        self.w = w

    def clear(self):
        w = self.w
        h = self.h
        self.img = Image.new("RGB", (h, w), Color.getColor())

    def save(self, name):
        self.img.save(name)

    def setPixel(self, y, x, color):
        self.img.putpixel((x, y), color.getColor())

    def drawRectangle(self, x, y, h, w, color):
        for a in range(x, h):
            for b in range(y, w):
                self.setPixel(a, b, color)

"""
#Example;
#creating color and image
color = Color(50, 150, 50)
img = Frame(100, 100, color)

#set random black points
import random
color = Color(0, 0, 0)
for i in range(0, 1000):
    x = random.randint(0, 99)
    y = random.randint(0, 99)
    img.setPixel(x, y, color)
    
#draw red reactangle(attention, axes!)
img.drawRectangle(50, 50, 75, 90, Color(255, 0, 0))

#saving image
img.save("test.png")
"""
