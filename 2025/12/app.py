import re

def rotate(matrix):
    n = len(matrix)
    split_matrix = [""]*n
    for idx, str in enumerate(matrix):
        split_matrix[idx] = list(str)
    # Transpose
    for i in range(n):
        for j in range(i, n):
            split_matrix[i][j], split_matrix[j][i] = split_matrix[j][i], split_matrix[i][j]
    # Reverse each row
    for i in range(n):
        split_matrix[i].reverse()
    
    for idx, chars in enumerate(split_matrix):
        matrix[idx] = "".join(chars)

class Gift:
    def __init__(self, lines_):
        self.id = ""
        self.shape = []
        for line in lines_:
            if ":" in line:
                pair = line.split(":")
                if (pair[1] == "\n"):
                    self.id = int(pair[0])
            else:
                self.shape.append(line.strip())
    
    def min_width(self):
        min = None
        for sh in self.shape:
            sh_min = sh.count ("#")
            if min is None or sh_min < min:
                min = sh_min
        return min
    
    def min_length(self):
        rotated = self.shape.copy ()
        rotate(rotated)
        min = None
        for sh in rotated:
            sh_min = sh.count ("#")
            if min is None or sh_min < min:
                min = sh_min
        return min

    def print(self):
        for sh in self.shape:
            print(sh)

class Region:
    def __init__(self, pair_):
        size = pair_[0].split("x")
        self.width = int(size[0])
        self.length = int(size[1])
        self.gifts = [int(x) for x in pair_[1].strip().split(" ")]

    def area(self):
        return self.width * self.length
    
    def print(self):
        print(f"Width {self.width}")
        print(f"length {self.length}")
        print(f"Gifts {self.gifts}")

def process_region(gifts_, region_:Region):
    '''
    Process known scenarios 
    1. If total gifts can fit taking up the full 3*3 space they can all fit
    2. If the area of the region is smaller than total # in gifts, they can't fit
    3. 
    '''
    total_sq_units = 0
    #  Total min width/height was a flawed logic
    # total_min_width = 0
    # total_min_length = 0
    total_gifts = 0

    for idx, gift_count in enumerate(region_.gifts):
        gift_sq_units = 0
        # total_min_width += gifts_[idx].min_width() * gift_count
        # total_min_length += gifts_[idx].min_length() * gift_count
        
        for sh in gifts_[idx].shape:
            gift_sq_units += sh.count("#")
        total_sq_units += gift_sq_units * gift_count
        total_gifts += gift_count

    gift_limit = (region_.width // 3) * (region_.length // 3)

    if gift_limit > total_gifts:
        return True
    # if region_.width < total_min_width and region_.width < total_min_length:
    #     return False
    # if region_.length < total_min_width and region_.length < total_min_length:
    #     return False
    if total_sq_units > region_.area():
        return False
    
    
    return True


def process(input_):
    '''
    Process the input data
    
    :param input_: File input data
    '''
    gifts = {}
    gift_lines = []
    regions = []
    for line in input_:
        if line == "\n":
            gift:Gift = Gift(gift_lines)
            gifts[gift.id] = gift
            gift_lines.clear ()
            continue
        else:
            if (":" in line):
                pair = line .split(":")
                if pair[1] != "\n":
                    regions.append(Region(pair))
            gift_lines.append(line)

    for gift in gifts.values():
        print (f"W:{gift.min_width()} L:{gift.min_length()}")

    valid_regions = 0
    for reg in regions:
        if process_region(gifts, reg):
            valid_regions += 1
    return valid_regions

with open('2025/12/input.txt') as f:
    print (f"Total: {process(f.readlines())}")
