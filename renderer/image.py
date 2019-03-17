from PIL import Image

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


# class containing? loading and saving images. Wrap for PIL
class Frame:
    img = None
    h = 0
    w = 0

    def __init__(self, w, h, color):
        self.img = Image.new("RGB", (h, w), color.getColor())
        self.h = h
        self.w = w

    # saves the image
    def save(self, name):
        self.img.save(name)

    def setPixel(self, x, y, color):
        try:
            self.img.putpixel((int(x), int(y)), color.getColor())
        except:
            # print(x, y)
            pass

    # drawing rectangle with start at (x,y) and finsh at (w,h)
    def drawRectangle(self, x, y, h, w, color):
        for a in range(int(x), int(h)):
            for b in range(int(y), int(w)):
                self.setPixel(a, b, color)

    # drawing texture(like drawRectangle, but texture instead of simple color)
    def drawTexture(self, x, y, h, w, texture, x1, y1, cellW, cellH):
        text = Image.open(texture)
        for i in range(int(x), int(h)):
            for j in range(int(y), int(w)):

                try:
                    color = text.getpixel((
                        int(abs(x1 / cellW + y1 / cellH - int(x1 / cellW + y1 / cellH)) * text.size[1]),
                        abs(int(text.size[1] / ((y - w)) * (j - w)))))
                except:
                    color = (0, 0, 0)

                self.setPixel(i, j, Color(color[0], color[1], color[2]))

    # init image with the simple background
    def makeWorld(self):
        self.img = Image.open("renderer/res/background.jpg")
