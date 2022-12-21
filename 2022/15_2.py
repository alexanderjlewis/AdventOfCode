from pathlib import Path
from time import time
from copy import deepcopy

t0 = time()

################ Data Processing #################

fin = (Path(__file__).parent / "in/test/15.in") #(ANS1=26,ANS2=56000011)
#fin = (Path(__file__).parent / "in/15.in")

sensors = []
beacons = []

with open(fin, "r") as f:
    data = f.read().replace("Sensor at x=","").replace(" y=","").replace(": closest beacon is at x=",",").replace(", y=","")
    data = data.split("\n")
    data = [x.split(",") for x in data]
    for row in data:
        sx,sy,bx,by = map(int,row)
        d = abs(sx-bx) + abs(sy-by)
        sensors.append(tuple([sx,sy,d]))
        beacons.append(tuple([bx,by]))

y_val = 10
#y_val = 2000000

################ Common Function #################



################ Part 1 #################

no_beacon = set()

for sx,sy,d in sensors:
    if abs(y_val-sy) <= d:
        for dx in range(-d+abs(y_val-sy),d+1-abs(y_val-sy)):
            if (abs(dx) + abs(y_val-sy)) <= d:
                no_beacon.add((sx+dx,y_val))

count = len(no_beacon)
for _,y in beacons:
    if y == y_val:
        count -= 1

print('ans1:',count)

################ Part 2 #################

dirs = [(1,1),(-1,1),(1,-1),(-1,-1)]
 
for sx,sy,d in sensors:

    for i in range(d+2):
        
        for x_sign,y_sign in dirs:
            x_off = i * x_sign
            y_off = (d - i) * y_sign

            tx,ty = sx+x_off, sy+y_off

            intersected = False

            if (0<=tx<=4_000_000) and (0<=ty<=4_000_000):
                for sx2, sy2, d2 in sensors:
                    if (abs(sx2-tx) + abs(sy2-ty)) <= d:
                        intersected = True

            if not intersected:
                break
        
        if not intersected:
                break
    
    if not intersected:
                break
        
print(tx,ty)


print('ans2:',(tx*4_000_000)+ty)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))