from typing import Optional
import copy

data = []
total_splits = 0

class Point:
    '''
    Holds X/Y point values, allowing deep copy and validation checking
    '''
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def copy(self):
        return copy.deepcopy(self)

    def is_valid(self):
        return self.x != None and self.y != None
    x: Optional[int] = None
    y: Optional[int] = None

def trace_beam (beam_: Point, time_lines_: int):
    '''
    Recursively trace a beams total possible paths
    
    :param beam_: Starting point of beam
    :type beam_: Point
    :param time_lines_: Total number of timelines from accumulated
    :type time_lines_: int
    '''
    global data
    global total_splits
    if (not beam_.is_valid() or beam_.y >= len(data) or beam_.y < 0
            or beam_.x >= len(data[0]) or beam_.x < 0):
        return time_lines_
    item = data[beam_.y][beam_.x]
    if item == "^":
        beam1 = beam_.copy ()
        beam2 = beam_.copy ()
        beam1.x += 1
        beam2.x -= 1
        total_splits +=1
        new_timelines = 0
        new_timelines += trace_beam (beam1, time_lines_)
        new_timelines += trace_beam (beam2, time_lines_)
        return new_timelines
    if item == ".":
        beam1 = beam_.copy ()
        beam1.y += 1
        val = trace_beam (beam1, time_lines_)
        # Stash the total so we don't recalculate the same path
        data[beam_.y][beam_.x] = val
        return val
    # Already calculated path return results
    return data[beam_.y][beam_.x]

def fire_laser(laser_pos_: Point):
    '''
    Start the path from the lasers position
    
    :param laser_pos_: Point at which the laser "S" exists
    :type laser_pos_: Point
    '''
    global data
    if not laser_pos_:
        return "Laser not found"
    laser_pos_.y += 1
    print (f"Total timelines:{trace_beam (laser_pos_, 1)}")


def find_laser():
    '''
    Find the point that contains the laser "S"
    '''
    global data
    for row_idx,row in enumerate(data):
        for col_idx,col in enumerate(row):
            if col == "S":
                return Point(col_idx, row_idx)
    return Point()

def process(input_):
    '''
    Process the input data and generate the matrix, then fire the laser
    
    :param input_: File input data
    '''
    global data
    global total_splits
    data = [[0]]*len(input_)
    for i,line in enumerate(input_):
        data[i] = list(line.rstrip())
    fire_laser(find_laser())
    for line in data:
        print (line)
    return total_splits


with open('2025/07/input.txt') as f:
    print("Part 1 Total: %s" %(process(f.readlines())))

