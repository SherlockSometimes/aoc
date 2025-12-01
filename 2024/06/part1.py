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

character = ['<','>','^','v']
traveled = [[]]
grid = []

def getDirection(character):
    if character == '<':
        return position_t(0,-1)
    if character == '>':
        return position_t(0,1)
    if character == '^':
        return position_t(-1,0)
    if character == 'v':
        return position_t(1,0)
    print("ERROR: unknown character")

def getData(input):
    data = [[0]]*len(input)
    for i,line in enumerate(input):
        data[i] = list(line.rstrip())
    global found
    found = [['.' for i in range(len(data[0]))] for j in range(len(input))]
    return data

tempList = []
def findWord(grid, startPos, direction):
    currPos = position_t(startPos.row, startPos.col)
    tempList.clear ()
    global found
    for letter in XMAS:
        if (currPos.row < 0 or currPos.row > grid.rows - 1
            or currPos.col < 0 or currPos.col > grid.cols - 1):
            return False
        if grid.data[currPos.row][currPos.col] == letter:
            tempList.append((position_t(currPos.row, currPos.col),letter))
            if letter == XMAS[-1]:
                for pair in tempList:
                    found[pair[0].row][pair[0].col] = pair[1]
                return True
            currPos.row += direction.row
            currPos.col += direction.col
            continue
        return False
    return True

def travelDirections(direction, startPos):
    count = 0
    if findWord(grid,startPos,direction):
        count += 1
    return count

def search():
    global grid
    count = 0
    for row in range(grid.rows):
        for col in range(grid.cols):
            if grid.data[row][col] in character:
                travelDirections(getDirection(grid.data[row][col]), position_t(row,col))
    return count

def main(input):
    global grid
    grid = wordSearch ()
    grid.setData(getData(input))

    # return search()


with open('06/test.txt') as f:
    print("Total: %s" %(main(f.readlines())))

for row in grid.data:
    print(row)