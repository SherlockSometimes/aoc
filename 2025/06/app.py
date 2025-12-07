import re

data = []

def do_math (symbols_):
    global data
    totals = 0
    for idx, symbol in enumerate(symbols_):
        total = 0
        if symbol == "*":
            for row_idx, row in enumerate(data):
                if row_idx == 0:
                    total = row[idx]
                    continue
                total = row[idx] * total
            totals += total
        if symbol == "+":
            for row_idx, row in enumerate(data):
                total += row[idx]
            totals += total
    return totals

def process_part_1(input_):
    global data
    for idx,line in enumerate(input_):
        if idx == len(input_) -1:
            return do_math (re.split(r'\s+',line.strip()))
        item = [int(x) for x in re.split(r'\s+',line.strip())]
        data.append (item.copy ())

def process_part_2(input_):
    value_set = []
    overall_total = 0
    for i in range(len(input_[0].replace("\n", "")), 0, -1):
        value = ""
        total = 0
        for line_idx,line in enumerate(input_):
            char = line.replace("\n", "")[i-1]
            if char == "+":
                value_set.append (int(value))
                for val in value_set:
                    total += val
                overall_total += total
                value_set.clear ()
                continue
            if char == "*":
                value_set.append (int(value))
                for val_idx,val in enumerate(value_set):
                    if val_idx == 0:
                        total = val
                        continue
                    total = total * val
                overall_total += total
                value_set.clear ()
                continue
            value += char
        if value.strip () == "":
            value_set.clear ()
            continue
        value_set.append (int(value))
    return overall_total


            

with open('2025/06/input.txt') as f:
    print("Part 1 Total: %s" %(process_part_1(f.readlines())))
with open('2025/06/input.txt') as f:
    print("Part 2 Total: %s" %(process_part_2(f.readlines())))
