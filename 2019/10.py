from pathlib import Path
from time import time
import math
import collections

t0 = time()

################ Data Processing #################

lines = (Path(__file__).parent / "in/10.in").open().readlines()
data = [list(line.replace('\n','')) for line in lines]

h = len(data)
w = len(data[0])

################ Part 1 #################

d = {}

ans1 = 0
ans1_dict = {}

for x in range(w):
    for y in range(h):
        d.clear()
        for x1 in range(w):
            for y1 in range(h):
                if not(x1 == x and y1 == y):
                    if data[y1][x1] == '#':
                        a = (math.atan2(y-y1,x-x1) + (1.5 * math.pi)) % (2 * math.pi)
                        if a in d:
                            d[a].append((x1,y1))
                        else:
                            d[a] = [(x1,y1)]
        if len(d) > ans1:
            ans1 = len(d)
            ans1_dict = d.copy()

print('ans1:',ans1)

################ Part 2 #################

ans1_dict = collections.OrderedDict(sorted(ans1_dict.items()))
ans2 = ans1_dict[list(ans1_dict.keys())[199]][0]

print('ans2:',ans2[0]*100 + ans2[1])

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))