import re

mulPattern = "[m][u][l][(][0-9]{1,3}[,][0-9]{1,3}[)]"
doPattern = "[d][o][(][)]"
dontPattern = "[d][o][n]['][t][(][)]"

patterns = [mulPattern, doPattern, dontPattern]
regex = re.compile('|'.join(patterns))

def getAllMatches(line):
    matches = re.findall(regex, line)
    print(matches)
    return matches

def evaluate(mul):
    matches = re.findall("[0-9]{1,3}", mul)
    print(matches)
    return int(matches[0]) * int(matches[1])

def validateMemory(input):
    total = int(0)
    print("Total Lines: %s" %(len(input)))
    enabled = True
    for line in input:
        for mul in getAllMatches(line):
            if (re.match(doPattern, mul)):
                enabled = True
                continue
            if (re.match(dontPattern, mul)):
                enabled = False
                continue
            if enabled:
                total += evaluate(mul)
    return total

with open('03/input.txt') as f:
# with open('03/test2.txt') as f:
    print("Total: %s" %(validateMemory(f.readlines())))