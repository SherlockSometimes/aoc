import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

from ctypes import c_uint

zeroCount = int(0)
currentIndex = int(0)

def full_loop(count: c_uint):
    '''
    Increment zero count for each full loop in count
    '''
    global zeroCount
    global currentIndex
    mod = count % 100
    zeroCount += (count - mod) / 100

def R(count: c_uint):
    '''
    Turn dial right by count
    '''
    global zeroCount
    global currentIndex
    logger.debug(f"Moving {currentIndex} R {count}")
    if (count > 99):
        full_loop(count)
        count = count % 100
    if ((count + currentIndex) > 99):
        logger.debug(f"R Adjusting {count}")
        if (currentIndex != 0 and (count + currentIndex) > 100):
            zeroCount += 1
            logger.debug(f"Zero Count incremented: {zeroCount}")
        count = count - 100
        logger.debug(f"R Adjusted {count} {currentIndex}")
    currentIndex += count
    logger.debug(f"R Current Index: {currentIndex}")
    if (currentIndex == 0):
        zeroCount += 1
        logger.debug(f"Zero Count incremented: {zeroCount}")

def L(count: c_uint):
    '''
    Turn dial left by count
    '''
    global zeroCount
    global currentIndex
    logger.debug(f"Moving {currentIndex} L {count}")
    if (count > 99):
        full_loop(count)
        count = count % 100
    if ((currentIndex - count) < 0):
        logger.debug(f"L Adjusting {count}")
        if (currentIndex != 0 and (currentIndex - count) < 0):
            zeroCount += 1
            logger.debug(f"Zero Count incremented: {zeroCount}")
        count = count - 100
        logger.debug(f"L Adjusted {count} {currentIndex}")
    currentIndex = currentIndex - count
    logger.debug(f"L Current Index: {currentIndex}")
    if (currentIndex == 0):
        zeroCount += 1
        logger.debug(f"Zero Count incremented: {zeroCount}")

def process_line(lines):
    '''
    Loop through lines in input file and process command
    '''
    for line in lines:
        if line.startswith("L"):
            L(int(line.replace('L','').rstrip()))
        elif line.startswith("R"):
            R(int(line.replace('R','').rstrip()))

currentIndex = 50

with open('2025/01/input2.txt') as f:
    process_line(f.readlines())


logger.info(f"Zero Count: {zeroCount}")

