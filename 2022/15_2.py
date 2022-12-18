from pathlib import Path
from time import time
from copy import deepcopy

t0 = time()

################ Data Processing #################

fin = (Path(__file__).parent / "in/test/15.in") #(ANS1=26,ANS2=56000011)
#fin = (Path(__file__).parent / "in/15.in")

sensors = []
taken = []

with open(fin, "r") as f:
    data = f.read().replace("Sensor at x=","").replace(" y=","").replace(": closest beacon is at x=",",").replace(", y=","")
    data = data.split("\n")
    data = [x.split(",") for x in data]
    for row in data:
        sx,sy,bx,by = map(int,row)
        d = abs(sx-bx) + abs(sy-by)
        sensors.append(tuple([sx,sy,d]))
        taken.append(tuple([bx,by]))
        taken.append(tuple([sx,sy]))

y_val = 10
y_val = 2000000

################ Common Function #################

def all_coords_in_dist(base,dist):
    
    x,y = base
    dx = 0
    dy = y - y_val

    t1 = time()
    for dx in range(-dist,dist+1):
        if (abs(dx) + abs(dy)) <= dist:
            taken.add(tuple([x+dx,y_val]))
    print("Func: %dms" % (1000 * (time() - t1)))
    return

################ Part 1 #################

min_y = min(taken)[1]
max_y = max(taken)[1]

print(min_y,max_y)
'''
for sensor in sensors:
    sx,sy,d = sensors

    if man_dist > 0:
        all_coords_in_dist([sx,sy],man_dist)

count = 0

for item in taken:
    x,y = item
    if y == y_val:
        count += 1

for item in beacons:
    x,y = item
    if y == y_val:
        count -= 1'''

print('ans1:',count)

################ Part 2 #################


print('ans2:',)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))