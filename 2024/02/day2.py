def validate(lhs, rhs, ascending):
    # value not changing
    if lhs == rhs:
        return False
    # value changed direction
    if (ascending):
        if(lhs > rhs or (rhs - lhs > 3)):
            return False
    else:
        if(lhs < rhs or (lhs - rhs > 3)):
            return False
    return True

def removeAndCheck(levels, idx, corrected):
    if len(levels) == 1:
        raise ValueError('report too short.')
    updated_list = [e for i, e in enumerate(levels) if i != idx]
    return isSafe (updated_list, corrected)
    

# Returns number of errors in report
def isReportSafe(report):
    levels = [int(lhs) for lhs in report.split()]
    if len(levels) == 1:
        raise ValueError('report too short.')
    
    return isSafe(levels, False)

def isSafe(levels, corrected=False):
    ascending = False
    startVal = levels[0]
    nextVal = levels[1]
    if startVal == nextVal:
        if corrected:
            print(levels)
            return False
        else:
            return removeAndCheck(levels, 0, True)

    ascending =  startVal < nextVal
    skip = False
    for idx, lhs in enumerate(levels):
        # Last element, nothing left to check
        if (idx+1 >= len(levels)):
            return True
        rhs = levels[idx+1]
        # Valid keep moving
        if (validate(lhs, rhs, ascending)):
            continue

        if not corrected and idx == len(levels) - 2:
            return True

        # if previous error we are done its invalid
        if (corrected):
            print(levels)
            return False
        else:
            # If this is the second level try removing the first
            if (idx == 1 and removeAndCheck(levels, 0, True)):
                return True

        # Try removing current level
        if removeAndCheck(levels, idx, True):
            return True
        
        # If we aren't the last element, try removing the next element
        if idx < len(levels) - 2 and removeAndCheck(levels, idx+1, True):
            return True
        
        return False


def validateReports(reports):
    validCount = int(0)
    print("Total Reports: %s" %(len(reports)))
    for report in reports:
        if (isReportSafe(report)):
            validCount += 1
        else:
            print (report)
    return validCount

with open('02/input.txt') as f:
    print("Safe Reports: %s" %(validateReports(f.readlines())))