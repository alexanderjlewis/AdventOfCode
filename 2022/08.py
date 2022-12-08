from pathlib import Path
from time import time
from copy import deepcopy

t0 = time()

################ Data Processing #################

fin = (Path(__file__).parent / "in/test/08.in") #(ANS1=21,ANS2=)
#fin = (Path(__file__).parent / "in/08.in")

grid = []
with open(fin, "r") as f:
    grid = f.read()
    grid = [list(a) for a in grid.split("\n")]
    
grid_seen = deepcopy(grid)

################ Common Function #################


################ Part 1 #################

for i, row in enumerate(grid):
    for j, col in enumerate(row):
                

print('ans1:',grid)

################ Part 2 #################

print('ans2:',find_start(datastream,14))

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))