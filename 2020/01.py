from pathlib import Path
from time import time
from itertools import combinations
from math import prod

t0 = time()

################ Data Processing #################

fin = (Path(__file__).parent / "in/01.in").open()
entries = [int(x) for x in fin.readlines()]

target = 2020

################ Common Function #################

def comb(target,items):
    for x in combinations(entries, items):
        if sum(x) == target:
            return prod(x)

################ Part 1 #################

print('ans1:',comb(target,2))

################ Part 2 #################

print('ans2:',comb(target,3))

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))