from math import dist, prod
from itertools import combinations

data = set()

def find_existing_connection(circuits_, jb_):
    '''
    Look through existing circuits for the given junction box.
    If found return the circuit else return None
    
    :param circuits_: Circuits to search
    :param jb_: Junction Box to look for
    '''
    for cir in circuits_:
        if jb_ in cir:
            return cir
    return None

def calculate_circuits(connection_count_ = None):
    global data
    # Create a list of all possible unique combinations
    all_pairs = combinations(data, 2)
    # Sort by distance
    pairs = sorted(all_pairs, key=lambda pair: dist(*pair))
    circuits = []

    # Add the first pair
    circuits = []

    for idx, (jb1, jb2) in enumerate(pairs):
        # Remove junction boxes as we process
        data.discard(jb1)
        data.discard(jb2)

        # Create circuit from first pair
        if idx == 0:
            circuits.append(set(tuple([jb1,jb2])))
            continue

        # Limit set and reached
        if idx == connection_count_:
            sorted_list = sorted(circuits, key=len)
            return prod([len(x) for x in sorted_list[-3:]])
            

        # Find existing connections for each box
        connection1 = find_existing_connection(circuits,jb1)
        connection2 = find_existing_connection(circuits,jb2)

        # If they are both connected either they are already in the same
        # circuit or we need to combine two circuits
        if connection1 and connection2:
            if connection1 == connection2:
                continue
            else:
                connection1.update(connection2)
                circuits.remove(connection2)
            continue

        # If neither is connected create a new circuit
        if None == connection1 == connection2:
            circuits.append(set(tuple([jb1, jb2])))
            continue

        # Add the unconnected box to the existing connection
        if connection1:
            connection1.add(jb2)
        elif connection2:
            connection2.add(jb1)

        # If we reached the end of the set
        if not data:
            return jb1[0] * jb2[0]

def process(input_):
    '''
    Process the input data
    
    :param input_: File input data
    '''
    global data
    for i,line in enumerate(input_):
        data.add(tuple([int(x) for x in line.strip().split(",")]))

    print(f"Part 1: {calculate_circuits(1000)}")

    data.clear ()
    for i,line in enumerate(input_):
        data.add(tuple([int(x) for x in line.strip().split(",")]))
    print(f"Part 2: {calculate_circuits()}")
    return 


with open('2025/08/input.txt') as f:
    process(f.readlines())

