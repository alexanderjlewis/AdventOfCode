from pathlib import Path
from time import time
from copy import deepcopy

t0 = time()

################ Data Processing #################

fin = (Path(__file__).parent / "in/11.in").open().read()
numbers = fin.split('\n')
numbers = [list(number) for number in numbers]

################ Common Function #################

cols = len(numbers[0])
rows = len(numbers)

adjacency = [(i,j) for i in (-1,0,1) for j in (-1,0,1) if not (i == j == 0)] #the adjacency matrix

numbers_next = deepcopy(numbers)

def print_array(array1, array2):
    print('in:             next:')
    for i,item in enumerate(array1):
        str=''
        print(str.join(array1[i]),'    ',str.join(array2[i]),'    ',str.join(occ[i]))
    print('----')

while True:
    #for j in range(2):
    occ= [['-']*cols for _ in range(rows)]
    for x in range(0,cols):
        for y in range(0,rows):
            if numbers[y][x] == '.':
                continue

            occupied_seats = 0
            
            for dx, dy in adjacency:
                if 0 <= (x + dx) < cols and 0 <= (y + dy) < rows: #check boundaries
                    if numbers[y + dy][x + dx] == '#':
                        occupied_seats += 1
            occ[y][x] = str(occupied_seats)

            #print(x,y,occupied_seats)
            if numbers[y][x] == 'L' and occupied_seats == 0:
                numbers_next[y][x] = '#'
            elif numbers[y][x] == '#' and occupied_seats >= 4:
                numbers_next[y][x] = 'L'
            
            #print(occupied_seats)
    
    #print_array(numbers, numbers_next)

    if numbers == numbers_next:
        print('break')    
        break
    else:
        numbers = deepcopy(numbers_next)

################ Part 1 #################

print('ans1:',sum([number.count('#') for number in numbers]))

################ Part 2 #################

#print('ans2:',min(test_list) + max(test_list))

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))