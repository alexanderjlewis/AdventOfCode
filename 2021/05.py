
from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

lines = []

#fin = (Path(__file__).parent / "in/test/05.in") #(ANS1=5,ANS2=12)
fin = (Path(__file__).parent / "in/05.in")
with open(fin, "r") as f:
    for line in f:
        processed_line = line.strip().split(' -> ')
        processed_line = [tuple(map(int, coord.split(','))) for coord in processed_line]
        lines.append(processed_line)

################ Common Function #################

################ Part 1 #################

overlapping_points = {}

for line in lines:
    x1, y1 = line[0]
    x2, y2 = line[1]

    dx = x2 - x1
    dy = y2 - y1

    x_dir = 1
    y_dir = 1

    if (dx < 0):
        x_dir = -1
        
    if (dy < 0): #if the dx/dy are negative, swap the points around
        y_dir = -1

    if dx == 0: #vertical line
        for i in range(0,dy + y_dir,y_dir):
            new_point = (x1, y1 + i)
            if new_point in overlapping_points:
                overlapping_points[new_point] += 1
            else:
                overlapping_points[new_point] = 1
        
    elif dy == 0: #horizontal line
        #print('dy = 0')
        for i in range(0,dx + x_dir,x_dir):
            new_point = (x1 + i, y1)
            if new_point in overlapping_points:
                overlapping_points[new_point] += 1
            else:
                overlapping_points[new_point] = 1 

ans = 0
for point in overlapping_points:
    if overlapping_points[point] > 1:
        ans += 1
print('ans1:',ans)

################ Part 2 #################

overlapping_points = {}

for line in lines:
    x1, y1 = line[0]
    x2, y2 = line[1]

    dx = x2 - x1
    dy = y2 - y1

    x_dir = 1
    y_dir = 1

    if (dx < 0):
        x_dir = -1
        
    if (dy < 0): #if the dx/dy are negative, swap the points around
        y_dir = -1

    if dx == 0: #vertical line
        for i in range(0,dy + y_dir,y_dir):
            new_point = (x1, y1 + i)
            if new_point in overlapping_points:
                overlapping_points[new_point] += 1
            else:
                overlapping_points[new_point] = 1
        
    elif dy == 0: #horizontal line
        for i in range(0,dx + x_dir,x_dir):
            new_point = (x1 + i, y1)
            if new_point in overlapping_points:
                overlapping_points[new_point] += 1
            else:
                overlapping_points[new_point] = 1 
    
    else: #diagonal
        x_coords = [i for i in range(0,dx + x_dir,x_dir)]
        y_coords = [i for i in range(0,dy + y_dir,y_dir)]
        for i,j in zip( x_coords, y_coords ):
            new_point = (x1 + i, y1 + j)
            if new_point in overlapping_points:
                overlapping_points[new_point] += 1
            else:
                overlapping_points[new_point] = 1  

ans = 0
for point in overlapping_points:
    if overlapping_points[point] > 1:
        ans += 1
print('ans2:',ans)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))