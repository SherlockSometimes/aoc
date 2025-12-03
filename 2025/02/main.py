def isRepeating (num):
    val = str(num)
    digits = len(val)
    mid_point = int(digits/2)
    values = []
    for i in range(1,mid_point+1):
        values.clear ()
        for j in range(0, len(val), i):
            values.append(val[j:j + i])
        if (len(set(values)) == 1):
            return True
    return len(set(values)) == 1

def check_range(val_):
    ret = []
    parts = val_.split("-")
    for i in range(int(parts[0]), int(parts[1]) + 1):
        if isRepeating(i):
            ret.append(i)
    return ret

def process_lines (lines):
    doubles = []
    for line in lines:
        ranges = line.rstrip().split(",")
        for range in ranges:
            doubles.extend(check_range(range))
    print(f"The Sum is: {sum(doubles)}")

with open('2025/02/input.txt') as f:
    process_lines (f.readlines())