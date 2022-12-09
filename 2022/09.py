from pathlib import Path
from time import time
from copy import deepcopy

t0 = time()

################ Data Processing #################

fin = (Path(__file__).parent / "in/test/09.in") #(ANS1=13,ANS2=0)
fin = (Path(__file__).parent / "in/test/09_2.in") #(ANS1=,ANS2=36)
fin = (Path(__file__).parent / "in/09.in")

instructions = []
dirs = {"R":(1,0),"U":(0,1),"D":(0,-1),"L":(-1,0)} # x is +ve right, y is +ve up

with open(fin, "r") as f:
    data = f.read().split("\n")
    instructions = [tuple(a.split(" ")) for a in data]
    instructions = [[dirs[a],int(b)] for a,b in instructions]

################ Common Function #################

def follow_knot(x1,y1,x2,y2):

        if abs(x1 - x2) == 2 and abs(y1 - y2) == 2: #diagonal move
            if (x1 - x2) > 0:
                x2 += (x1 - x2 - 1)
            else:
                x2 += (x1 - x2 + 1)
            if (y1 - y2) > 0:
                y2 += (y1 - y2 - 1)
            else:
                y2 += (y1 - y2 + 1)

        elif abs(x1 - x2) == 2:
            if abs(y1 - y2) > 0:
                y2 = y1 
            if (x1 - x2) > 0:
                x2 += (x1 - x2 - 1)
            else:
                x2 += (x1 - x2 + 1)

        elif abs(y1 - y2) == 2:
            if abs(x1 - x2) > 0:
                x2 = x1
            if (y1 - y2) > 0:
                y2 += (y1 - y2 - 1)
            else:
                y2 += (y1 - y2 + 1)
        
        return x2,y2

################ Part 1 #################

x = [0] * 2
y = [0] * 2
tail_visited = set()

for row in instructions:
    dir,qty = row
    dx,dy = dir

    for _ in range(qty):

        x[0] += dx
        y[0] += dy

        x[1],y[1] = follow_knot(x[0],y[0],x[1],y[1])
        
        tail_visited.add(tuple([x[1],y[1]]))

print('ans1:',len(tail_visited))

################ Part 2 #################

x = [0] * 10
y = [0] * 10
tail_visited = set()

for row in instructions:
    dir,qty = row
    dx,dy = dir

    for _ in range(qty):

        x[0] += dx
        y[0] += dy

        for i in range(9):
            x[i+1],y[i+1] = follow_knot(x[i],y[i],x[i+1],y[i+1])
        
        tail_visited.add(tuple([x[9],y[9]]))

print('ans2:',len(tail_visited))

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))