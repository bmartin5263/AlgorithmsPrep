# 01 Matrix
# https://leetcode.com/problems/01-matrix/description/

UP = (0,1)
DOWN = (0,-1)
LEFT = (-1,0)
RIGHT = (1,0)

DIRECTIONS = (UP,DOWN,LEFT,RIGHT)

def printMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

def updateMatrix(matrix):
    updatedMatrix = []
    for i in range(len(matrix)):
        updatedMatrix.append([])
        matrixLen = len(matrix[i])
        for j in range(matrixLen):
            value = matrix[i][j]
            if value == 0:
                updatedMatrix[i].append(value)
            else:
                surroundingCells = []
                for direction in DIRECTIONS:
                    x = i+direction[0]
                    y = j+direction[1]
                    if (x >= 0 and x < matrixLen) and (y >= 0 and y < matrixLen):
                        cellVal = matrix[x][y]
                        surroundingCells.append(cellVal)
                value = min(surroundingCells) + 1
                updatedMatrix[i].append(value)

    return updatedMatrix

if __name__ == '__main__':
    m = [
        [1,1,1],
        [1,1,0],
        [1,1,0]
    ]
    printMatrix(m)
    print()
    n = updateMatrix(m)
    n = updateMatrix(n)
    printMatrix(n)