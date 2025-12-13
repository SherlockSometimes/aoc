class Device:
    def __init__(self,str_):
        parts = str_.strip().split(":")
        self.device = parts[0]
        self.outputs = parts[1].strip().split(" ")
    device=""
    outputs=[]

cache={}

def get_path_count (devices, you_, count_, hit_dac_ = None, hit_fft_ = None):
    global cache
    if "out" in you_.outputs:
        if (hit_dac_ == hit_fft_ == True) or (hit_dac_ is None and hit_fft_ is None):
            return count_ + 1
        return count_

    if tuple([you_.device, hit_dac_, hit_fft_]) in cache:
        return cache[you_.device, hit_dac_, hit_fft_]

    hit_dac, hit_fft = hit_dac_, hit_fft_
    if hit_dac_ == False:
        hit_dac = you_.device == "dac"
    if hit_fft_ == False:
        hit_fft = you_.device == "fft"

    count = 0
    for device in you_.outputs:
        count += get_path_count(devices, devices[device], count_, hit_dac, hit_fft)
    cache[tuple([you_.device, hit_dac_, hit_fft])] = count
    return count

def process(input_):
    '''
    Process the input data
    
    :param input_: File input data
    '''
    devices = {}
    for line in input_:
        dev = Device(line)
        devices[dev.device] = dev
    return get_path_count(devices, devices["you"], 0)

def process2(input_):
    '''
    Process the input data
    
    :param input_: File input data
    '''
    devices = {}
    for line in input_:
        dev = Device(line)
        devices[dev.device] = dev
    return get_path_count(devices, devices["svr"], 0, False, False)


# with open('2025/11/input.txt') as f:
#     print (f"Part 1:{process(f.readlines())}")

with open('2025/11/input.txt') as f:
    print (f"Part 2:{process2(f.readlines())}")

