
from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

#fin = (Path(__file__).parent / "in/07_test.in")
fin = (Path(__file__).parent / "in/07.in")
with open(fin, "r") as f:
   crab_list = f.read().split(',')
   crab_list = [int(x) for x in crab_list]

min_val = min(crab_list)
max_val = max(crab_list)

################ Common Function #################



################ Part 1 #################

fuel = []

for i in range(min_val,max_val):
    temp = 0
    for crab in crab_list:
        temp += abs(crab - i)
    fuel.append(temp)

print('ans1:',min(fuel))

################ Part 2 ################

fuel = []

for i in range(min_val,max_val):
    temp = 0
    for crab in crab_list:
        delta = abs(crab - i)
        temp += int((delta * (delta + 1))/2)
    fuel.append(temp)

print('ans2:',min(fuel))

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))