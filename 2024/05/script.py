rules = {}
updates = []

def splitLine (lines):
    processingRules = True
    global updates
    global rules
    for line in lines:
        if line == '\n':
            processingRules = False
            continue
        if processingRules:
            split = line.split("|")
            key = int(split[0])
            if not key in rules:
                rules[key] = [int(split[1].rstrip())]
            else:
                rules[key].append(int(split[1].rstrip()))
        else:
            updates.append([int(x) for x in line.rstrip().split(",")])
    # print(rules)
    # print(updates)

def checkUpdate (update):
    for idx,value in enumerate(update):
        if value in rules:
            for rule in rules[value]:
                if rule in update:
                    if idx < update.index(rule):
                        continue
                    else:
                        return False
    return True

def fixUpdate (update):
    for idx,value in enumerate(update):
        if value in rules:
            for rule in rules[value]:
                if rule in update:
                    if idx < update.index(rule):
                        continue
                    else:
                        update.insert(update.index(rule), update.pop(idx))
                        return fixUpdate(update)
    return update

def getMiddle(update):
    middleIndex = int((len(update) - 1)/2)
    return int(update[middleIndex])

with open('05/input.txt') as f:
    splitLine(f.readlines())

total = 0
totalFixed = 0
for update in updates:
    if (checkUpdate(update)):
        print(update)
        total += getMiddle(update)
    else:
        totalFixed += getMiddle(fixUpdate(update))

print ("Total: %d" %(total))
print ("Total Fixed: %d" %(totalFixed))