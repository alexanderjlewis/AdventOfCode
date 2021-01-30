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

ans1 = 0
ans1_dict = {}

def check_array(x,y,h,w,data):
    d = {}
    for x1 in range(w):
        for y1 in range(h):
            if not(x1 == x and y1 == y):
                if data[y1][x1] == '#':
                    angle = (math.atan2(y-y1,x-x1) + (1.5 * math.pi)) % (2 * math.pi)
                    if angle in d:
                        d[angle].append((x1,y1))
                    else:
                        d[angle] = [(x1,y1)]
    return d

for x in range(w):
    for y in range(h):
        d = check_array(x,y,h,w,data)
        if len(d) > ans1:
            ans1 = len(d)
            ans1_dict = d.copy()

print('ans1:',ans1)

################ Part 2 #################

target = 200

ans1_dict = collections.OrderedDict(sorted(ans1_dict.items()))
ans2 = ans1_dict[list(ans1_dict.keys())[target-1]][0]

print('ans2:',ans2[0]*100 + ans2[1])

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))