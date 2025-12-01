from ctypes import c_uint

zeroCount = int(0)
currentIndex = int(0)

def full_loop(count: c_uint):
    global zeroCount
    global currentIndex
    mod = count % 100
    zeroCount += (count - mod) / 100

def R(count: c_uint):
    global zeroCount
    global currentIndex
    # print (f"Moving {currentIndex} R {count}")
    if (count > 99):
        full_loop(count)
        count = count % 100
    if ((count + currentIndex) > 99):
        # print (f"R Adjusting {count}")
        if (currentIndex != 0 and (count + currentIndex) > 100):
            zeroCount += 1
            # print (f"Zero Count incremented: {zeroCount}")
        count = count - 100
        # print (f"R Adjusted {count} {currentIndex}")
    currentIndex += count
    # print (f"R Current Index: {currentIndex}")
    if (currentIndex == 0):
        zeroCount += 1
        # print (f"Zero Count incremented: {zeroCount}")

def L(count: c_uint):
    global zeroCount
    global currentIndex
    # print (f"Moving {currentIndex} L {count}")
    if (count > 99):
        full_loop(count)
        count = count % 100
    if ((currentIndex - count) < 0):
        # print (f"L Adjusting {count}")
        if (currentIndex != 0 and (currentIndex - count) < 0):
            zeroCount += 1
            # print (f"Zero Count incremented: {zeroCount}")
        count = count - 100
        # print (f"L Adjusted {count} {currentIndex}")
    currentIndex = currentIndex - count
    print (f"L Current Index: {currentIndex}")
    if (currentIndex == 0):
        zeroCount += 1
        # print (f"Zero Count incremented: {zeroCount}")

def process_line(lines):
    for line in lines:
        if line.startswith("L"):
            L(int(line.replace('L','').rstrip()))
        elif line.startswith("R"):
            R(int(line.replace('R','').rstrip()))

currentIndex = 50

with open('2025/01/input2.txt') as f:
    process_line(f.readlines())


print (f"Zero Count: {zeroCount}")

