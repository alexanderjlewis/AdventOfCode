from pathlib import Path
from time import time
from copy import deepcopy

t0 = time()

################ Data Processing #################

#fin = (Path(__file__).parent / "in/test/12.in") #(ANS1=31,ANS2=29)
fin = (Path(__file__).parent / "in/12.in")

grid = []
with open(fin, "r") as f:
    data = f.read().split("\n")
    grid = [list(map(ord,a)) for a in data]
   
width = len(grid[0])
height = len(grid)

for i in range(width):
    for j in range(height):
        if grid[j][i] == 83: #start
            start = (i,j)
            grid[j][i] = 1
        elif grid[j][i] == 69: #end
            end = (i,j)
            grid[j][i] = 26
        else:
            grid[j][i] = grid[j][i] - 96


################ Common Function #################

dirs = [(0,1),(1,0),(-1,0),(0,-1)]

################ Part 1 #################

def move_1(next):

    coord, cost = next
    cx, cy = coord 
    
    cont = False

    if costs[cy][cx] == '':
        costs[cy][cx] = cost
        cont = True
    elif cost < costs[cy][cx]:
        costs[cy][cx] = cost
        cont = True

    cost += 1

    if cont:
        
        for dir in dirs:
            dx, dy = dir
            nx = cx + dx
            ny = cy + dy
            if nx in range(width) and ny in range(height):
                if grid[ny][nx] <= (grid[cy][cx] + 1):
                    queue.append(((nx,ny),cost))

costs = [['' for i in range(width)] for j in range(height)]
visited = [[False for i in range(width)] for j in range(height)]
queue = [(start,0)]

while len(queue) > 0:
    move_1(queue.pop(0))

print('ans1:',costs[end[1]][end[0]])

################ Part 2 #################

def move_2(next):

    coord, cost = next
    cx, cy = coord 
    
    cont = False

    if costs[cy][cx] == '':
        costs[cy][cx] = cost
        cont = True
    elif cost < costs[cy][cx]:
        costs[cy][cx] = cost
        cont = True

    cost += 1

    if cont and grid[cy][cx] != 1:
        
        for dir in dirs:
            dx, dy = dir
            nx = cx + dx
            ny = cy + dy
            if nx in range(width) and ny in range(height):
                if grid[ny][nx] >= (grid[cy][cx] - 1):
                    queue.append(((nx,ny),cost))

costs = [['' for i in range(width)] for j in range(height)]
visited = [[False for i in range(width)] for j in range(height)]
queue = [(end,0)]
routes_to_a = []

while len(queue) > 0:
    move_2(queue.pop(0))

for i in range(width):
    for j in range(height):
        if grid[j][i] == 1:
            if costs[j][i]:
                routes_to_a.append(costs[j][i])

print('ans2:',min(routes_to_a))

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))