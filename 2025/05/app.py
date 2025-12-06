fresh_ranges = []

def is_fresh (id_):
    global fresh_ranges
    for i,range in enumerate(fresh_ranges):
        if id_ < range[0]:
            return False
        if i == len(fresh_ranges) and id_ > range[1]:
            return False
        if id_ > range[1]:
            continue
        return True

def reduce_ranges():
    global fresh_ranges
    reduced_ranges = []
    fresh_ranges.sort ()
    current_range = []
    for i,range in enumerate(fresh_ranges):
        if not current_range:
            current_range = range.copy()
            continue
        if current_range[1] < range[0]:
            reduced_ranges.append (current_range.copy ())
            current_range.clear ()
            current_range = range.copy()
            continue
        if range[1] < current_range[1]:
            continue
        current_range[1] = range[1]
        continue
    reduced_ranges.append (current_range.copy ())
    fresh_ranges = reduced_ranges

    total_fresh_ids = 0
    for range in fresh_ranges:
        total_fresh_ids += range[1] - range[0] + 1
    print (f"Total Fresh IDs: {total_fresh_ids}")
    return
        

def process_data(input_):
    global fresh_ranges
    getting_ranges = True
    fresh_count = 0
    for line in input_:
        if (line.rstrip() == ""):
            getting_ranges = False
            reduce_ranges()
            continue
        if getting_ranges:
            fresh_ranges.append([int(x) for x in line.rstrip().split('-')])
        else:
            if is_fresh(int(line.rstrip())):
                fresh_count += 1
    return fresh_count

with open('2025/05/input.txt') as f:
    print("Total: %s" %(process_data(f.readlines())))
