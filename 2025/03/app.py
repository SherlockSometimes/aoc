

def find_largest_int(val_: str):
    print(f"FindLargInt:{val_}")
    first_idx=0
    ret=0
    for index,char in enumerate(val_):
        if int(char) > ret:
            ret = int(char)
            first_idx = index
    return first_idx

def find_largest_joltage(val_:str):
    ret=""
    start_idx=0
    jolt_len=12
    for i in range(1,jolt_len+1):
        if (jolt_len-i) == 0:
            idx = find_largest_int(val_[start_idx:])
        else:
            idx = find_largest_int(val_[start_idx:-(jolt_len-i)])
        ret+=val_[idx+start_idx]
        start_idx+=idx+1
    print (ret)
    return int(ret)

def process_lines(lines):
    total_joltage=0
    for line in lines:
        total_joltage += find_largest_joltage(line.rstrip())
    print (f"Total Joltage:{total_joltage}")

with open('2025/03/input.txt') as f:
    process_lines(f.readlines())