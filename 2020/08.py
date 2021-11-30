from pathlib import Path
from time import time
import re

t0 = time()

################ Data Processing #################

fin = (Path(__file__).parent / "in/08.in").open().read()
instructions = fin.split('\n')
instructions = [instruction.replace('+','') for instruction in instructions]
instructions = [tuple(instruction.split(' ')) for instruction in instructions]
instructions = [(x, int(y)) for x, y in instructions] #cast the types

################ Common Function #################

################ Part 1 #################

instructions_part1 = instructions.copy()
pos = 0
acc = 0

while True:
    #print(instructions_part1,pos,acc)
    try:
        op, arg = instructions_part1[pos]
        instructions_part1[pos] = ''
    except:
        break

    if op == 'nop':
        pos += 1
    elif op == 'jmp':
        pos += arg
    elif op == 'acc':
        acc += arg
        pos += 1

print('ans1:',acc)

################ Part 2 #################

program_terminates = False

for i, instruction in enumerate(instructions):
    
    instructions_part2 = instructions.copy()
    
    op, arg = instruction
    if op == 'nop':
        instructions_part2[i] = ('jmp',arg)
    elif op == 'jmp':
        instructions_part2[i] = ('nop',arg)
    else:
        continue

    pos = 0
    acc = 0

    while True:
        try:
            op, arg = instructions_part2[pos]
            instructions_part2[pos] = ''
        except:
            break

        if op == 'nop':
            pos += 1
        elif op == 'jmp':
            pos += arg
        elif op == 'acc':
            acc += arg
            pos += 1

        if pos >= len(instructions_part2):
            program_terminates = True
            break

    if program_terminates:
        print('ans2:',acc)
        break

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))


'''

import re
import math
import copy

fin = open("data.in")
lines = [line.strip() for line in fin.readlines() if line.strip()]
visited = set()
acc = 0
pos = 0
max_index = 0

#print(lines)

lines = [line.replace('+','') for line in lines]
lines = [line.split(' ') for line in lines]

temp_lines = copy.deepcopy(lines)
max_index = len(lines)

for i in range(max_index):
    

    


'''