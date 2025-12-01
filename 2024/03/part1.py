import re

def getAllMatches(line):
    matches = re.findall("[m][u][l][(][0-9]{1,3}[,][0-9]{1,3}[)]", line)
    print(matches)
    return matches

def evaluate(mul):
    matches = re.findall("[0-9]{1,3}", mul)
    print(matches)
    return int(matches[0]) * int(matches[1])

def validateMemory(input):
    total = int(0)
    print("Total Lines: %s" %(len(input)))
    for line in input:
        for mul in getAllMatches(line):
            total += evaluate(mul)
    return total


with open('03/input.txt') as f:
    print("Total: %s" %(validateMemory(f.readlines())))