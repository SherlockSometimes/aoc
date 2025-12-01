from enum import Enum

class wordSearch:
    def setData(self, newData):
        self.data = newData
        self.rows = len(newData)
        self.cols = len(newData[0])

    data = [[]]
    rows = 0
    cols = 0

class position_t:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    row = 0
    col = 0

found = [[]]

def getData(input):
    data = [[0]]*len(input)
    for i,line in enumerate(input):
        data[i] = list(line.rstrip())
    global found
    found = [['.' for i in range(len(data[0]))] for j in range(len(input))]
    return data

forwardDir = [ position_t(1,-1),position_t(-1,1)]
backwardDir = [position_t(-1,-1),position_t(1,1)]

XMAS = list("MAS")
tempList = []
def findWord(grid, startPos):
    currPos = position_t(startPos.row, startPos.col)
    tempList.clear ()
    global found
    x1 = position_t(startPos.row + forwardDir[0].row, startPos.col + forwardDir[0].col)
    x2 = position_t(startPos.row + forwardDir[1].row, startPos.col + forwardDir[1].col)
    y1 = position_t(startPos.row + backwardDir[0].row, startPos.col + backwardDir[0].col)
    y2 = position_t(startPos.row + backwardDir[1].row, startPos.col + backwardDir[1].col)

    # make sure all coords are valid
    if (x1.row < 0 or x1.row > grid.rows - 1 or x1.col < 0 or x1.col > grid.cols - 1 
         or y1.row < 0 or y1.row > grid.rows - 1 or y1.col < 0 or y1.col > grid.cols - 1 or
        x2.row < 0 or x2.row > grid.rows - 1 or x2.col < 0 or x2.col > grid.cols - 1 
         or y2.row < 0 or y2.row > grid.rows - 1 or y2.col < 0 or y2.col > grid.cols - 1):
        return False

    # check fox X
    if (((grid.data[x1.row][x1.col] == "M" and grid.data[x2.row][x2.col] == "S") 
         or (grid.data[x1.row][x1.col] == "S" and grid.data[x2.row][x2.col] == "M")) and
        ((grid.data[y1.row][y1.col] == "M" and grid.data[y2.row][y2.col] == "S")
         or (grid.data[y1.row][y1.col] == "S" and grid.data[y2.row][y2.col] == "M"))):
            found[startPos.row][startPos.col] = 'A'
            found[x1.row][x1.col] = grid.data[x1.row][x1.col]
            found[x2.row][x2.col] = grid.data[x2.row][x2.col]
            found[y1.row][y1.col] = grid.data[y1.row][y1.col]
            found[y2.row][y2.col] = grid.data[y2.row][y2.col]
            return True
    return False

def search(grid):
    count = 0
    for row in range(grid.rows):
        for col in range(grid.cols):
            if grid.data[row][col] == 'A':
                if findWord(grid, position_t(row,col)):
                    count += 1
    return count

def main(input):
    grid = wordSearch ()
    grid.setData(getData(input))

    return search(grid)


with open('04/input.txt') as f:
    print("Total: %s" %(main(f.readlines())))

# for row in found:
#     print(row)