
from pathlib import Path
from time import time
from copy import deepcopy

t0 = time()

################ Data Processing #################

energy_levels = []

#fin = (Path(__file__).parent / "in/test/11.in") #(ANS1=1656,ANS=195)
fin = (Path(__file__).parent / "in/11.in")
with open(fin, "r") as f:
    for line in f:
        line = list(line.strip())
        line = [int(x) for x in line]
        energy_levels.append(line)

################ Common Function #################

adjacency = [(i,j) for i in (-1,0,1) for j in (-1,0,1) if not (i == j == 0)] #the adjacency matrix 
rows = len(energy_levels)
cols = len(energy_levels[0])

steps = 100
flashes = 0

def add_one(array):
    for i, row in enumerate(array):
        array[i] = [x+1 for x in row]
    return array

def model_step(array,flashes):    
    
    array = add_one(array)

    nine_found = True
    
    while nine_found == True:

        nine_found = False

        for row in range(rows):
            for col in range(cols):
                if array[row][col] > 9:
                    flashes += 1
                    array[row][col] = 0
                    nine_found = True

                    for dx, dy in adjacency:
                        if 0 <= (col + dx) < cols and 0 <= (row + dy) < rows: #check boundaries
                            if array[row + dy][col + dx] > 0:
                                array[row + dy][col + dx] += 1

    return array, flashes

################ Part 1 #################


energy_levels1 = deepcopy(energy_levels)

for i in range(steps):
    energy_levels1, flashes = model_step(energy_levels1, flashes)

print('ans1:',flashes)

################ Part 2 ################

energy_levels2 = deepcopy(energy_levels)
steps = 0

while True:
    energy_levels2, flashes = model_step(energy_levels2, flashes)
    steps += 1

    if sum([sum(x) for x in energy_levels2]) == 0:
        break

print('ans2:',steps)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))