from pathlib import Path
from time import time
from copy import deepcopy

t0 = time()

################ Data Processing #################

fin = (Path(__file__).parent / "in/11.in").open().read()
seat_layout = fin.split('\n')
seat_layout = [list(row) for row in seat_layout]

################ Common Function #################

cols = len(seat_layout[0])
rows = len(seat_layout)

adjacency = [(i,j) for i in (-1,0,1) for j in (-1,0,1) if not (i == j == 0)] #the adjacency matrix

def print_array(array1, array2):
    print('in:             next:')
    for i,item in enumerate(array1):
        str=''
        print(str.join(array1[i]),'    ',str.join(array2[i]))
    print('----')

################ Part 1 #################

seat_layout_1 = deepcopy(seat_layout)
seat_layout_1_next = deepcopy(seat_layout_1)

while True:
    for x in range(0,cols):
        for y in range(0,rows):
            if seat_layout_1[y][x] == '.':
                continue

            occupied_seats = 0
            
            for dx, dy in adjacency:
                if 0 <= (x + dx) < cols and 0 <= (y + dy) < rows: #check boundaries
                    if seat_layout_1[y + dy][x + dx] == '#':
                        occupied_seats += 1

            if seat_layout_1[y][x] == 'L' and occupied_seats == 0:
                seat_layout_1_next[y][x] = '#'
            elif seat_layout_1[y][x] == '#' and occupied_seats >= 4:
                seat_layout_1_next[y][x] = 'L'

    #print_array(seat_layout_1,seat_layout_1_next)

    if seat_layout_1 == seat_layout_1_next:
        break
    else:
        seat_layout_1 = deepcopy(seat_layout_1_next)

    
print('ans1:',sum([row.count('#') for row in seat_layout_1]))

################ Part 2 #################

seat_layout_2 = deepcopy(seat_layout)
seat_layout_2_next = deepcopy(seat_layout_2)

while True:
    for x in range(0,cols):
        for y in range(0,rows):
            if seat_layout_2[y][x] == '.':
                continue

            occupied_seats = 0
             
            for dx, dy in adjacency:
                
                x_test = x
                y_test = y
                
                while True:
                    x_test += dx
                    y_test += dy
                    if 0 <= x_test < cols and 0 <= y_test < rows: #check boundaries
                        if seat_layout_2[y_test][x_test] == '#':
                            occupied_seats += 1
                            break
                        elif seat_layout_2[y_test][x_test] == 'L':
                            break
                    else:
                        break

            if seat_layout_2[y][x] == 'L' and occupied_seats == 0:
                seat_layout_2_next[y][x] = '#'
            elif seat_layout_2[y][x] == '#' and occupied_seats >= 5:
                seat_layout_2_next[y][x] = 'L'
    
    #print_array(seat_layout_2,seat_layout_2_next)

    if seat_layout_2 == seat_layout_2_next:
        break
    else:
        seat_layout_2 = deepcopy(seat_layout_2_next)

print('ans2:',sum([row.count('#') for row in seat_layout_2]))

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))