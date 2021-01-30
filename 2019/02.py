from pathlib import Path
from time import time
from lib.intcode import IntcodeComp

t0 = time()

################ Data Processing #################

lines = (Path(__file__).parent / "in/02.in").open().read().split(',')
instructions = {}
for i, val in enumerate(lines):
    instructions[i] = int(val)

################ Part 1 #################

computer = IntcodeComp(instructions)
computer.inst[1] = 12
computer.inst[2] = 2
computer.compute()

print('ans1:',computer.inst[0])

################ Part 2 #################

goal = 19690720

for i in range(100):
    for j in range(100):
        computer = IntcodeComp(instructions)
        computer.inst[1] = i
        computer.inst[2] = j
        computer.compute()
        print('ans2:',100*i+j) if computer.inst[0] == goal else next

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))
