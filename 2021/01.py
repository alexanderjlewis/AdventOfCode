from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

#fin = (Path(__file__).parent / "in/01_test.in").open().read()
fin = (Path(__file__).parent / "in/01.in").open().read()
measurements = fin.split('\n')
measurements = [int(measurement) for  measurement in measurements]

################ Common Function #################

################ Part 1 #################

counter_1 = 0

for i, measurement in enumerate(measurements[:-1]):
    if measurements[i] < measurements[i+1]:
        counter_1 += 1

print('ans1:',counter_1)

################ Part 2 #################

counter_2 = 0

for i, measurement in enumerate(measurements[:-3]):
    group1 = sum(measurements[i:i+3])
    group2 = sum(measurements[i+1:i+4])
    if group1 < group2:
        counter_2 += 1

print('ans2:',counter_2)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))