from pathlib import Path
from time import time
from copy import deepcopy

t0 = time()

################ Data Processing #################

#fin = (Path(__file__).parent / "in/test/14.in") #(ANS1=24,ANS2=93)
fin = (Path(__file__).parent / "in/14.in")

rock_coords = []
with open(fin, "r") as f:
    data = f.read().split("\n")
    for row in data:
        row = row.split(" -> ")
        rock_coords.append(row)
    
################ Common Function #################

def coords_to_set(coords):
    rocks = set()

    for line in coords:
        for i in range(1,len(line)):
            x0,y0 = map(int,line[i-1].split(","))
            x1,y1 = map(int,line[i].split(","))
            if x0 == x1: #horizontal rock line
                if y1 > y0:
                    for j in range(y1-y0+1):
                        rocks.add(tuple([x0,y0+j]))
                else:
                    for j in range(y0-y1+1):
                        rocks.add(tuple([x0,y1+j]))
            else: #vertical rock line
                if x1 > x0:
                    for j in range(x1-x0+1):
                        rocks.add(tuple([x0+j,y0]))
                else:
                    for j in range(x0-x1+1):
                        rocks.add(tuple([x1+j,y0]))

    return rocks

def find_max_y(coords):
    max_y = 0
    for coord in coords:
        _,y = coord
        if y > max_y:
            max_y = y

    return max_y

blocked = coords_to_set(rock_coords)
rocks_max_y = find_max_y(blocked)

################ Part 1 #################

blocked_1 = deepcopy(blocked)

sand = 0

end = False

while not end:
    sand_x = 500
    sand_y = 0

    while True:
        
        if tuple([sand_x,sand_y+1]) in blocked_1:
            if tuple([sand_x-1,sand_y+1]) in blocked_1:
                if tuple([sand_x+1,sand_y+1]) in blocked_1:
                    blocked_1.add(tuple([sand_x,sand_y]))
                    sand += 1
                    break
                else:
                    sand_y += 1
                    sand_x += 1
            else:
                sand_y += 1
                sand_x -= 1
        else:
            sand_y += 1
                    
        if sand_y > (rocks_max_y + 1):
            end = True
            break
        
print('ans1:',sand)

################ Part 2 #################

floor = rocks_max_y + 1

blocked_2 = deepcopy(blocked)

sand = 0

while tuple([500,0]) not in blocked_2:

    sand_x = 500
    sand_y = 0

    while True:
        
        if tuple([sand_x,sand_y+1]) in blocked_2:
            if tuple([sand_x-1,sand_y+1]) in blocked_2:
                if tuple([sand_x+1,sand_y+1]) in blocked_2:
                    blocked_2.add(tuple([sand_x,sand_y]))
                    sand += 1
                    break
                else:
                    sand_y += 1
                    sand_x += 1
            else:
                sand_y += 1
                sand_x -= 1
        else:
            sand_y += 1
                    
        if sand_y == floor:
            blocked_2.add(tuple([sand_x,sand_y]))
            sand += 1
            break
        
print('ans2:',sand)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))