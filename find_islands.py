class FI():

    ISLAND = 'X'
    WATER = 'O'

    def __init__(self, array, rows, columns):
        self.rows = rows
        self.columns = columns
        self.map = array
        self.mapLen = len(array)
        self.found = [False for i in range(self.mapLen)]
        self.islands = 0
        self.directions = (-1,1,self.columns,-self.columns)

    def findIslands(self):
        for i, letter in enumerate(self.map):
            if not self.found[i]:
                if letter == self.ISLAND:
                    self.islands += 1
                    self.visitIsland(i)
                else:
                    self.found[i] = True
        print(self.islands)

    def visitIsland(self, location):
        self.found[location] = True
        leftEdge = location % 4 == 0
        rightEdge = location % 4 == 3
        for movement in self.directions:
            if (movement == -1 and leftEdge) or (movement == 1 and rightEdge):
                pass
            else:
                newLocation = location + movement
                if 0 <= newLocation < self.mapLen:
                    if not self.found[newLocation] and self.map[newLocation] == self.ISLAND:
                        self.visitIsland(newLocation)

if __name__ == '__main__':
    islandMap = ['O','O','O','X',
                 'O','X','O','X',
                 'O','O','O','X',
                 'X','X','X','X']

    f = FI(islandMap,4,4)
    f.findIslands()
