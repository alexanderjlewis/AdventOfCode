from pathlib import Path
from time import time
from itertools import combinations

t0 = time()

################ Data Processing #################

fin = (Path(__file__).parent / "in/09.in").open().read()
numbers = fin.split('\n')
numbers = [int(number) for number in numbers]

################ Common Function #################

preamble = 25

################ Part 1 #################

for i, number in enumerate(numbers):
    if i < preamble:
        continue
    
    sums = []
    sums = [sum(pair) for pair in combinations(numbers[(i-preamble):i],2)]
    
    if number in sums:
        continue
    else:
        print('ans1:',number)
        break

################ Part 2 #################

sum_goal = number #from part 1

starting_index = 0
test_list = []
found = False

while sum(test_list) != sum_goal:

    test_list = []
    
    for number in numbers[starting_index:]:
        
        test_list.append(number)
        if sum(test_list) >= sum_goal:
            break

    starting_index += 1

print('ans2:',min(test_list) + max(test_list))

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))