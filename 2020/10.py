
from math import comb
from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

fin = (Path(__file__).parent / "in/10.in").open().read()
numbers = fin.split('\n')
numbers = [int(number) for number in numbers]

################ Common Function #################

################ Part 1 #################

number = numbers.sort()
numbers.insert(0,0)

gap_1 = 0
gap_3 = 0

for i, number in enumerate(numbers[:-1]):
    upper = numbers[i+1]
    lower = numbers[i]
    if upper-lower == 3:
        gap_3 += 1
    else:
        gap_1 += 1

gap_3 += 1 # need to add one additional gap of three to cover off the last hop to the device

print('ans1:',gap_1 * gap_3)

################ Part 2 #################

'''
Gaps of 3 only have one arrangement, given max gap = 3
Gaps of 1 have multiple arrangements depening on how many '1' gaps occur in a row:
    -1: 1 arrangement (1*1)
    -2: 2 arrangements (2*1, 1*2)
    -3: 4 arrangements (3*1, 1*2 + 1*1, 1*1 + 1*2)
    -4: 7 arrangements (4*1, 2*2, 1*2 + 2*1, 2*1 + 1*2, 1*1 + 1*2 + 1*1, 3*1 + 1*1, 1*1 + 3*1)
Analysis of raw data shows that a max of 4 '1' gaps occcur in a row so no need to consider above that
'''

count_1gaps_in_row = 0
combo_factors = {0:1,1:1,2:2,3:4,4:7}
combinations = 1

for i, number in enumerate(numbers[:-1]):
    upper = numbers[i+1]
    lower = numbers[i]
    if upper-lower == 3:
        combinations = combinations * combo_factors[count_1gaps_in_row]
        count_1gaps_in_row = 0
    else:
        count_1gaps_in_row += 1

print('ans2:',combinations)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))