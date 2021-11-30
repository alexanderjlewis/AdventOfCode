from pathlib import Path
from time import time
import math

t0 = time()

################ Data Processing #################

passes = (Path(__file__).parent / "in/05.in").open().readlines()

################ Common Function #################

seat_ids = []

################ Part 1 #################

for bpass in passes:
    row_code, col_code = bpass[:7], bpass[7:]

    row_range = (0,127)
    col_range = (0,7)

    for char in row_code:
        if char == 'B':
            row_range = (math.ceil(sum(row_range)/2) , row_range[1])
        else:
            row_range = (row_range[0] , math.floor(sum(row_range)/2))

    for char in col_code:
        if char == 'R':
            col_range = (math.ceil(sum(col_range)/2), col_range[1])
        else:
            col_range = (col_range[0],math.floor(sum(col_range)/2))

    seat_ids.append((row_range[1] * 8) + col_range[1])

print('ans1:',max(seat_ids))

################ Part 2 #################

seat_ids.sort()

for i, seat in enumerate(seat_ids):
    if seat + 2 == seat_ids[i+1]:
        print('ans2:',seat + 1)
        break

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))