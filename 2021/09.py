
from pathlib import Path
from time import time
from math import prod

t0 = time()

################ Data Processing #################

locations = []

#fin = (Path(__file__).parent / "in/test/09.in") #(ANS1=15,ANS2=1134)
fin = (Path(__file__).parent / "in/09.in")
with open(fin, "r") as f:
    for line in f:
        line = list(line.strip())
        line = [int(x) for x in line]
        locations.append(line)

################ Common Function #################

adjacency = [(i,j) for i in (-1,0,1) for j in (-1,0,1) if not ((i == j == 0) or (abs(i) == abs(j) == 1))] #the adjacency matrix (no diagonals)

cols = len(locations[0])
rows = len(locations)

################ Part 1 #################

low_points = []

def lowest_point(x,y):
    current_height = locations[y][x]
    lowest = True

    for dx, dy in adjacency:
        if 0 <= (x + dx) < cols and 0 <= (y + dy) < rows: #check boundaries
            #print('test:',locations[y + dy][x + dx])
            if locations[y + dy][x + dx] <= current_height:
                lowest = False

    return lowest

for y, row in enumerate(locations):
    for x, pos in enumerate(row):
        if lowest_point(x,y):
            low_points.append(int(pos))

print('ans1:',sum(low_points) + len(low_points))

################ Part 2 ################

checked_locations = []

def surrounded_by_9(x,y):
    count = 0

    for dx, dy in adjacency:
        if 0 <= (x + dx) < cols and 0 <= (y + dy) < rows: #check boundaries
            if (x + dx,y + dy) not in checked_locations:
                checked_locations.append((x+dx,y+dy))
                if locations[y + dy][x + dx] != 9:
                    count += 1
                    count += surrounded_by_9(x+dx,y+dy)

    return count

basins = []

for y, row in enumerate(locations):
    for x, pos in enumerate(row):
        if (x,y) in checked_locations:
            continue
        else:
            basins.append(surrounded_by_9(x,y))

basins.sort()

print('ans2:',prod(basins[-3:]))

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))