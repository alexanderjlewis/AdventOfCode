from pathlib import Path
from time import time
from copy import deepcopy

t0 = time()

################ Data Processing #################

fin = (Path(__file__).parent / "in/test/18.in") #(ANS1=64,ANS2=58)
fin = (Path(__file__).parent / "in/18.in")

lava = []
with open(fin, "r") as f:
    data = f.read().split("\n")
    lava = [tuple(map(int,x.split(','))) for x in data]
    
################ Common Function #################



################ Part 1 #################

possible_air = set()

sides = 6 * len(lava)

dirs = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]

for block in lava:
    x,y,z = block

    for dir in dirs:
        dx,dy,dz = dir

        if tuple([x+dx,y+dy,z+dz]) in lava:
            sides -= 1

print('ans1:',sides)

################ Part 2 #################

count_air = 0

max_x = max([x for x,y,z in lava]) + 1
max_y = max([y for x,y,z in lava]) + 1
max_z = max([z for x,y,z in lava]) + 1

min_x = min([x for x,y,z in lava]) - 1
min_y = min([x for x,y,z in lava]) - 1
min_z = min([x for x,y,z in lava]) - 1

queue = set()
queue.add(tuple([min_x,min_y,min_z]))

surface_area = 0

water = set()

while queue:

    x,y,z = queue.pop()

    water.add(tuple([x,y,z]))

    for dir in dirs:
        dx,dy,dz = dir
        nx,ny,nz = x+dx,y+dy,z+dz

        if (min_x<=nx<=max_x) and (min_y<=ny<=max_y) and (min_z<=nz<=max_z):
            if tuple([nx,ny,nz]) in lava:
                surface_area += 1
            else:
                if tuple([nx,ny,nz]) not in water:
                    queue.add(tuple([nx,ny,nz]))
                
print('ans2:',surface_area)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))