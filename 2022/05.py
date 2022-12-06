from pathlib import Path
from time import time
from copy import deepcopy

t0 = time()

################ Data Processing #################

#fin = (Path(__file__).parent / "in/test/05.in") #(ANS1="CMZ",ANS2=)
fin = (Path(__file__).parent / "in/05.in")

procedures = []
stacks = []

with open(fin, "r") as f:
    data = f.read()
    drawing, procedure_data = data.split("\n\n")   

    procedure_data = procedure_data.replace('move ',"").replace(' to ',",").replace(' from ',",")
    procedures = [list(map(int,a.split(','))) for a in procedure_data.split("\n")]

    drawing = drawing.replace('    ','#').replace('[',"").replace(']',"").replace(' ',"")
    drawing = [list(a) for a in drawing.split("\n")]

    cols = len(drawing[:-1])
    
    drawing = drawing[:-1]
    drawing = list(zip(*drawing[::-1]))

    for entry in drawing:
        a = ''.join(entry).replace('#','')
        stacks.append(a)
        
  
################ Common Function #################



################ Part 1 #################

stacks_part1 = deepcopy(stacks)

for procedure in procedures:
    
    x, col_fr, col_to = procedure
    col_fr -= 1
    col_to -= 1
    for i in range(x):
        stacks_part1[col_fr], char = stacks_part1[col_fr][:-1], stacks_part1[col_fr][-1]
        stacks_part1[col_to] = stacks_part1[col_to] + char

top_crates = [stack[-1] for stack in stacks_part1]

print('ans1:',''.join(top_crates))

################ Part 2 #################

stacks_part2 = deepcopy(stacks)

for procedure in procedures:
    
    x, col_fr, col_to = procedure
    col_fr -= 1
    col_to -= 1
    stacks_part2[col_fr], char = stacks_part2[col_fr][:-x], stacks_part2[col_fr][-x:]
    stacks_part2[col_to] = stacks_part2[col_to] + char

top_crates = [stack[-1] for stack in stacks_part2]

print('ans2:',''.join(top_crates))

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))