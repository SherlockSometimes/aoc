from enum import Enum

class grid:
    def __init__(self, input_):
        self.data = [[0]]*len(input_)
        for i,line in enumerate(input_):
            self.data[i] = list(line.rstrip())

    def find_rolls(self):
        '''
        Find rolls of paper in the grid and populate self.found
        '''
        self.found.clear ()
        for row_index, row in enumerate(self.data):
            for col_index, item in enumerate(row):
                if item == '@':
                    self.found.append(position_t(row_index, col_index))
        self.rows = len(self.data)
        self.cols = len(self.data[0])

    def value (self, row_, col_):
        '''
        Get the value of a position in the grid.
        If row or column is out of bounds and empty string is returned.
        :param row_: Row of item to check
        :param col_: Column of item to check
        '''
        if row_ < 0 or col_ < 0 or row_ >= len(self.data) or col_ >= len(self.data[row_]):
            return ""
        return self.data[row_][col_]

    data = [[]]
    rows = 0
    cols = 0
    found = []

class position_t:
    '''
    Holds a row and column
    '''
    def __init__(self, row, col):
        self.row = row
        self.col = col

    row = 0
    col = 0


#List of relative positions which are adjacent to a given position
RELATIVE_ADJACENT = [position_t(1,-1),
            position_t(1,0),
            position_t(1,1),
            position_t(0,-1),
            position_t(0,1),
            position_t(-1,-1),
            position_t(-1,0),
            position_t(-1,1)]

def can_access(grid, startPos: position_t):
    '''
    Check if a forklift can access a given position
    
    :param grid: The grid to check
    :param startPos: The position to check
    '''
    currPos = position_t(startPos.row, startPos.col)
    global RELATIVE_ADJACENT
    relative_adjacent_paper_count = 0
    for cell in RELATIVE_ADJACENT:
        x = currPos.row + cell.row
        y = currPos.col + cell.col
        if grid.value(x, y) == "@":
            relative_adjacent_paper_count += 1
    if relative_adjacent_paper_count >= 4:
        return False

    return True

def search(grid):
    '''
    Search a grid for the number of paper rolls that can be removed
    
    :param grid: The grid to search
    '''
    total = 0
    while True:
        count = 0
        grid.find_rolls()
        for pos in grid.found:
            if can_access (grid, pos):
                count += 1
                grid.data[pos.row][pos.col] = "."
        if count == 0:
            break
        total += count

    return total

with open('2025/04/input.txt') as f:
    print("Total: %s" %(search(grid (f.readlines()))))
