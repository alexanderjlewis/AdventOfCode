
from pathlib import Path
from time import time
from copy import deepcopy
from math import ceil

t0 = time()

################ Data Processing #################

points = []
instructions = []

#fin = (Path(__file__).parent / "in/test/15.in") #(ANS1=40,ANS2=315)
fin = (Path(__file__).parent / "in/15.in")
with open(fin, "r") as f:
    data = f.read()
    risk_level = data.splitlines()
    risk_level = [list(map(int,list(x))) for x in risk_level]

################ Common Function #################

adjacency = [(-1,0),(0,-1),(1,0),(0,1)]

def run(risk_level_array):
    cols = len(risk_level_array[0])
    rows = len(risk_level_array)

    min_risk_array = [[''] * (cols) for _ in range(rows)]

    def process_array(changed=False):
        for y in range(rows):
            for x in range(cols):
                if x==0 and y==0:
                    min_risk_array[0][0] = 0
                else:
                    prev_options = []
                    for dx, dy in adjacency:
                        if 0 <= (x+dx) < cols and 0 <= (y+dy) < rows: #check boundaries & previously visited
                            val = min_risk_array[y+dy][x+dx]
                            if val != '':
                                prev_options.append(val)
                        
                    if not prev_options:
                        prev_options = [0]
                    
                    new_val = min(prev_options) + risk_level_array[y][x]
                    if min_risk_array[y][x] != new_val:
                        changed = True
                        min_risk_array[y][x] = new_val
        
        return changed
        
    changed = True
    while changed == True:
        changed = process_array()
        
    return min_risk_array[-1][-1]

################ Part 1 #################

risk_level_part1 = deepcopy(risk_level)
risk_level_part1[0][0] = 0

print('ans1:',run(risk_level_part1))

################ Part 2 ################

def cap_at_9(x):
    if x > 9:
        x -= 9
    return x

risk_level_part2 = deepcopy(risk_level)

#duplicate the array horizontally 4 times, adding one each iteration
for i in range(len(risk_level)):
    for j in range(4):
        risk_level_part2[i].extend([cap_at_9(x+j+1) for x in risk_level[i]])

#duplicate the array verticaly 4 times, adding one each iteration
for j in range(4):
    for i in range(len(risk_level_part2)):
        risk_level_part2.append([cap_at_9(x+j+1) for x in risk_level_part2[i]])

risk_level_part2[0][0] = 0

print('ans2:',run(risk_level_part2))

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))