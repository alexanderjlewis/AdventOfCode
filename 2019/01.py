from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

fin = (Path(__file__).parent / "in/01.in").open()
rawData = [int(x) for x in fin.readlines()]

################ Part 1 #################

print('ans1:',sum(a // 3 - 2 for a in rawData))

################ Part 2 #################

def fuel_needed(b):
    b = b // 3 - 2
    return (b + fuel_needed(b) if b > 0 else 0)

print('ans2:',sum(fuel_needed(a) for a in rawData))

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))
