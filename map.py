class Map:
    w = 9;
    h = 8
    mapArr = """
111111111
110000001
100111001
100100001
100111101
100000101
100000001
111111111
"""

    # First index is 0!!!
    def get(self, x, y):
        # +1 for starting \n
        return self.mapArr[x * (self.w + 1) + y + 1]

    def empty(self, x, y):
        if "0" == self.mapArr[x * (self.w + 1) + y + 1]:
            return True
        return False
