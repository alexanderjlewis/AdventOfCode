from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

lines = (Path(__file__).parent / "in/03.in").open().read().split('\n')
d = [x.split(',') for x in lines]

################ Part 1 #################

def find_coords(d):
    out = dict()
    x = 0 
    y = 0
    counter = 0
    deltas_dict = {'R':(0,1),'D':(-1,0),'U':(1,0),'L':(0,-1)}

    for item in d:
        a = item[0]
        b = int(item[1:])
        dx, dy = deltas_dict[a]
        for i in range(b):
            y += dy
            x += dx
            counter += 1
            if (x,y) not in out:
                out[(x,y)] = counter
    return out

dict1 = find_coords(d[0])
dict2 = find_coords(d[1])
match = dict1.keys() & dict2.keys()

print('ans1:',min([sum([abs(ele) for ele in coords]) for coords in match]))

################ Part 2 #################

print('ans2:',min([(dict1[coords] + dict2[coords]) for coords in match]))

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))
