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
            print(x, y)

    def drawRectangle(self, x, y, h, w, color):
        for a in range(int(x), int(h)):
            for b in range(int(y), int(w)):
                self.setPixel(a, b, color)

    def drawTexture(self, x, y, h, w, texture, cellW, cellH):
        text = Image.open(texture)
        for i in range(int(x), int(h)):
            for j in range(int(y), int(w)):
                int1 = int((i / cellW - int(x / cellW)) * int(cellW))
                int2 = int((j / cellW - int(x / cellH)) * int(cellH))
                if(
                        (j % int(abs(x - h)))%text.size[1]==0 or
                        ((int1 + int2) % abs(int(y - w))) % text.size[0]==0
                ): color = text.getpixel((10,10))
                else:
                    try:
                        color = text.getpixel((
                            (j % int(abs(x - h)))%text.size[0],
                            ((int1 + int2) % abs(int(y - w))) % text.size[1],
                        ))
                    except: print((j % int(abs(x - h)))%text.size[1],
                            ((int1 + int2) % abs(int(y - w))) % text.size[0])
                self.setPixel(i, j, Color(color[0], color[1], color[2]))

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
