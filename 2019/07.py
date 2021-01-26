from pathlib import Path
from time import time
import itertools
from lib.intcode import IntcodeComp

t0 = time()

################ Data Processing #################

lines = (Path(__file__).parent / "in/07.in").open().read().split(',')
instructions = {}
for i, val in enumerate(lines):
    instructions[i] = int(val)

################ Part 1 #################

def thrust(seq):
    amps = []
    for item in seq:
        amps.append(IntcodeComp(instructions,[item]))

    val = 0
    for amp in amps:
        val = amp.compute([val])
    return val

print('ans1:',max(thrust(seq) for seq in list(itertools.permutations([0,1,2,3,4]))))

################ Part 2 #################

def thrust2(seq):
    amps = []
    for item in seq:
        amps.append(IntcodeComp(instructions,[item]))

    val = 0
    while True:
        temp = val
        for amp in amps:
            val = amp.compute([val])
        if val == None:
            val = temp
            break
    return val

print('ans2:',max(thrust2(seq) for seq in list(itertools.permutations([5,6,7,8,9]))))

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))
