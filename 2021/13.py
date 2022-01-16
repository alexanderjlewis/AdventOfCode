
from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

points = []
instructions = []

#fin = (Path(__file__).parent / "in/test/13.in") #(ANS1=17,ANS2=N/A)
fin = (Path(__file__).parent / "in/13.in")
with open(fin, "r") as f:
    data = f.read()
    points,instructions = data.split('\n\n')
    
    points = [tuple(map(int,point.split(','))) for point in points.splitlines()]
    
    instructions = [tuple(instruction.replace('fold along ','').split('=')) for instruction in instructions.splitlines()]
    instructions = [(a,int(b)) for a,b in instructions]

################ Common Function #################

def fold(axis,val,points):
    if axis == 'x':
        points = [(val - (x-val) if x > val else x,y) for x,y in points]
    else:
        points = [(x,val - (y-val) if y > val else y) for x,y in points]   
    return points

################ Part 1 #################

axis,val = instructions[0]
points = fold(axis,val,points)
points = list(set(points))

print('ans1:',len(points))

################ Part 2 ################

for axis,val in instructions:
    points = fold(axis,val,points)

points = list(set(points))

mx = max(x for x,y in points) + 1
my = max(y for x,y in points) + 1

out = [["  "] * (mx) for _ in range(my)]

for x,y in points:
    out[y][x] = "##"

print('ans2:')
for r in out:
    print("".join(r))

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))