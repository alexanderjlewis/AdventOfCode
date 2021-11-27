from pathlib import Path
from time import time
from math import prod

t0 = time()

################ Data Processing #################

lines = (Path(__file__).parent / "in/03.in").open().readlines()

################ Common Function #################

def trees_hit(slope):
    x,y = (0,0)
    y_inc, x_inc = slope

    trees_hit = 0

    while True:
        y += y_inc #add 3 onto the horiztonal pos
        x += x_inc
        if x >= len(lines):
            break
        if (lines[x][y % 31] == '#'):
            trees_hit += 1
    return trees_hit

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

out = []
for slope in slopes:
    out.append(trees_hit(slope))

################ Part 1 #################

print('ans1:',out[1])

################ Part 2 #################


print('ans2:',prod(out))

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))