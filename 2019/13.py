from pathlib import Path
from time import time, sleep
from lib.intcode import IntcodeComp
from PIL import Image
import os

t0 = time()

################ Data Processing #################

lines = (Path(__file__).parent / "in/13.in").open().read().split(',')
instructions = {}
for i, val in enumerate(lines):
    instructions[i] = int(val)

################ Part 1 #################

computer = IntcodeComp(instructions)

block_counter = 0

while True:
    o1, o2, o3 = computer.compute(), computer.compute(), computer.compute()

    if o1 == None:
        break

    if o3 == 2:
        block_counter += 1

print('ans1:',block_counter)

################ Part 2 #################

computer = IntcodeComp(instructions)
computer.inst[0] = 2

output = {}
score = 0
next_in = []

def next_calc(i):
    o1, o2, o3 = computer.compute(i), computer.compute(), computer.compute()
    return o1, o2, o3

ball_x = 0
paddle_x = 0

for i in range(836):
    o1, o2, o3 = next_calc([])
    output[(o1,o2)] = o3
    if o3 == 4:
        ball_x = o1
    elif o3 == 3:
        paddle_x = o1

while True:
    o1, o2, o3 = next_calc(next_in)
    next_in = []
    if computer.waiting_for_input == True:
        if ball_x == paddle_x:
            next_in = [0]
        elif ball_x > paddle_x:
            next_in = [1]
        elif ball_x < paddle_x:
            next_in = [-1]
    elif o1 == -1 and o2 == 0:
        score = o3
    elif o1 == None or o2 == None or o3 == None:
        break
    else:
        output[(o1,o2)] = o3
        if o3 == 4:
            ball_x = o1
        elif o3 == 3:
            paddle_x = o1

################ Timing #################

print('ans2:',score)

print("Time taken: %dms" % (1000 * (time() - t0)))