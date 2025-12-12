from shapely.geometry import Point, Polygon

data_points= []

def get_area(point1_, point2_):
    # p1.X < p2.X && p1.Y < p2.Y
    if (point1_[0] <= point2_[0] and point1_[1] <= point2_[1]):
        # point1_ == #top_left
        top_left = point1_
        bottom_right = point2_
    elif (point1_[0] >= point2_[0] and point1_[1] >= point2_[1]):
        # point1_ == #bottom_right
        top_left = point2_
        bottom_right = point1_
    elif (point1_[0] >= point2_[0] and point1_[1] <= point2_[1]):
        # point1_ == #top_right
        top_left = [point2_[0], point1_[1]]
        bottom_right = [point1_[0], point2_[1]]
    else:
        # point1_ == #bottom_left
        top_left = [point1_[0], point2_[1]]
        bottom_right = [point2_[0], point1_[1]]

    width = bottom_right[0] - top_left[0] + 1
    height = bottom_right[1] - top_left[1] + 1
    return height * width

def process(input_):
    '''
    Process the input data
    
    :param input_: File input data
    '''
    global data
    data = [[0]]*len(input_)
    for i,line in enumerate(input_):
        data[i] = [int(x) for x in line.strip().split(",")]

def part_1():
    global data
    max_area = 0
    for idx,point in enumerate(data):
        for i in range(idx+1, len(data)):
            area = get_area(point, data[i])
            if (area > max_area):
                max_area = area
    return max_area

def part_2():
    global data
    max_area = 0
    polygon = Polygon(data)
    for idx,point in enumerate(data):
        for i in range(idx+1, len(data)):
            polygon2 = Polygon([point, [point[0], data[i][1]], data[i], [data[i][0], point[1]]])
            if not polygon2.within(polygon):
                continue
            area = get_area(point, data[i])
            if (area > max_area):
                max_area = area
    return max_area

with open('2025/09/input.txt') as f:
    process(f.readlines())
    print("Total: %s" %(part_1 ()))
    print("Total 2: %s" %(part_2 ()))

