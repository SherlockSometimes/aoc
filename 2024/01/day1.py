listA, listB = [], []
totalDistance = int (0)
totalSimilarity = int (0)

def splitLine (lines):
    for line in lines:
        split = line.split("   ")
        listA.append(int(split[0]))
        listB.append(int(split[1]))
    listA.sort ()
    listB.sort ()

def findDistance ():
    for idx, x in enumerate(listA):
        global totalDistance
        totalDistance += abs(x - listB[idx])

def findSimilarity():
    for val in listA:
        global totalSimilarity
        totalSimilarity += val * listB.count(val)


with open('01/input.txt') as f:
    splitLine(f.readlines())

findDistance ()
findSimilarity ()

print ("Distance: %d" %(totalDistance))
print ("Similarity %d" %(totalSimilarity))