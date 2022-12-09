from pathlib import Path
from time import time
from copy import deepcopy

t0 = time()

################ Data Processing #################

fin = (Path(__file__).parent / "in/test/08.in") #(ANS1=21,ANS2=)
fin = (Path(__file__).parent / "in/08.in")

grid = []
with open(fin, "r") as f:
    grid = f.read()
    grid = [list(map(int,a)) for a in grid.split("\n")]
    
width,height = len(grid[0]), len(grid)

################ Common Function #################

def check_row(i,grid,grid_seen):

    grid_seen[i][0] = "#"
    max_h = grid[i][0]
    for j in range(1,width):
        if grid[i][j] > max_h:
            grid_seen[i][j] = "#"
            max_h = grid[i][j]

    grid_seen[i][width-1] = "#"
    max_h = grid[i][width-1]
    for j in range(width-2,0,-1):
        if grid[i][j] > max_h:
            grid_seen[i][j] = "#"
            max_h = grid[i][j]

    return grid, grid_seen

################ Part 1 #################

grid_1 = deepcopy(grid)
grid_seen = deepcopy(grid_1)

for i in range(height):
    grid_1,grid_seen = check_row(i,grid_1,grid_seen)

#rotate the grids by 90 degress
grid_1 = [list(a) for a in list(zip(*grid_1[::-1]))]
grid_seen = [list(a) for a in list(zip(*grid_seen[::-1]))]
width,height = len(grid_1[0]), len(grid_1)

for i in range(height):
    grid_1,grid_seen = check_row(i,grid_1,grid_seen)

count = sum(row.count('#') for row in grid_seen)     

print('ans1:',count)

################ Part 2 #################

dirs = [(1,0),(0,1),(-1,0),(0,0-1)]

width,height = len(grid[0]), len(grid)

scenic_scores = []
for i in range(width):
    for j in range(height):
        
        pos_score = 1
        
        for dir in dirs:
            x_step, y_step = dir
            x = i + x_step
            y = j + y_step

            count = 0
            while True:
                
                if x in range(width) and y in range(height):
                    count += 1
                    if grid[x][y] >= grid[i][j]:
                        break
                else:
                    break 

                x = x + x_step
                y = y + y_step
            
            pos_score = pos_score * count
                
        scenic_scores.append(pos_score)   

print('ans2:',max(scenic_scores))

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))