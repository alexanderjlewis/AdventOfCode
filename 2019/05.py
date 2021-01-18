from pathlib import Path
from time import time
from lib.intcode import IntcodeComp

t0 = time()

################ Data Processing #################

lines = (Path(__file__).parent / "in/05.in").open().read().split(',')
instructions = {}
for i, val in enumerate(lines):
    instructions[i] = int(val)

################ Part 1 #################

computer = IntcodeComp(instructions.copy())
computer.compute([1])
while computer.compute() == 0:
    next
print('ans1:',computer.out)

################ Part 2 #################

computer = IntcodeComp(instructions.copy())
print('ans2:',computer.compute([5]))

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))
