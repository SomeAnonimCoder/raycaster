import math


class Map:
    w = 10
    h = 15
    mapArr = """
111111111111111
100000000100001
100000111100001
100000000000001
100110000011101
100000000000001
100000000000001
100011111100001
100000000000001
111111111111111
"""

    # Axes: x -->, y - down

    # First index is 0!!!
    def get(self, y,x):
        # +1 for starting \n
        return self.mapArr[math.floor(y) * math.floor(self.w+1) + math.floor(x) + 1]

    def empty(self, y, x):
        print(x,y)
        if "0" == self.mapArr[math.floor(y) * math.floor(self.w+1) + math.floor(x) + 1]:
            return True
        return False
