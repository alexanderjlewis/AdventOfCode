
from pathlib import Path
from time import time
from copy import deepcopy

t0 = time()

################ Data Processing #################

connections = []

#fin = (Path(__file__).parent / "in/test/12_0.in") #(ANS1=10,ANS=36)
#fin = (Path(__file__).parent / "in/test/12_1.in") #(ANS1=19,ANS2=103)
#fin = (Path(__file__).parent / "in/test/12_2.in") #(ANS1=226,ANS2=3509)
fin = (Path(__file__).parent / "in/12.in")
with open(fin, "r") as f:
    for line in f:
        line = line.strip()
        a,b = line.split('-')
        connections.append((a,b))

################ Common Function #################

start = 'start'
end = 'end'

small_caves = []
for connection in connections:
    a,b = connection
    small_caves.append(a)
    small_caves.append(b)
small_caves = list(set(small_caves))
small_caves = [cave for cave in small_caves if cave.islower()]

################ Part 1 #################

def next_step1(path,connections):
    from_node = path[-1]
    
    next_paths = []
    next_pairs = []

    for connection in connections:
        if from_node in connection:
            next_pairs.append(connection)

    if next_pairs:
        for pair in next_pairs:
            temp_path = path[:]

            to_node = list(pair)
            to_node.remove(from_node)
            to_node = to_node[0]

            temp_path.append(to_node)

            if to_node == end:
                next_paths.append(temp_path)
            else: 
                temp_connections = connections.copy()
                connections_to_remove = []

                if from_node in small_caves:                   
                    connections_to_remove = [connection for connection in temp_connections if from_node in connection]
                
                temp_connections = [connection for connection in temp_connections if connection not in connections_to_remove]
                next_paths.extend(next_step1(temp_path,temp_connections))
    else:
        pass

    return next_paths

paths = []

paths.extend(next_step1(['start'],connections))
        
print('ans1:',len(paths))

################ Part 2 ################

def next_step2(path,connections,one_visit_caves,two_visit_caves):
    from_node = path[-1]
    
    next_paths = []
    next_pairs = []

    for connection in connections:
        if from_node in connection:
            next_pairs.append(connection)

    if next_pairs:
        for pair in next_pairs:
            temp_path = path[:]

            to_node = list(pair)
            to_node.remove(from_node)
            to_node = to_node[0]

            temp_path.append(to_node)
            temp_two_visit_caves = two_visit_caves.copy()
            temp_one_visit_caves = one_visit_caves.copy()

            if to_node == end:
                next_paths.append(temp_path)
            else: 
                temp_connections = connections.copy()
                connections_to_remove = []

                if (from_node in small_caves) and (from_node in temp_one_visit_caves):
                    connections_to_remove = [connection for connection in temp_connections if from_node in connection]
                elif (from_node in small_caves) and (from_node in temp_two_visit_caves):                  
                    connections_to_remove = [connection for connection in temp_connections if from_node in connection]
                    for item in temp_two_visit_caves:
                        connections_to_remove.extend([connection for connection in temp_connections if item in connection])
                    temp_one_visit_caves = small_caves.copy()

                elif from_node in small_caves:
                    temp_two_visit_caves.append(from_node)

                temp_connections = [connection for connection in temp_connections if connection not in connections_to_remove]
                next_paths.extend(next_step2(temp_path,temp_connections,temp_one_visit_caves,temp_two_visit_caves))
    else:
        pass

    return next_paths


one_visit_caves = [start,end]
two_visit_caves = []

paths = []

paths.extend(next_step2(['start'],connections,one_visit_caves,two_visit_caves))

print('ans2:',len(paths))

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))