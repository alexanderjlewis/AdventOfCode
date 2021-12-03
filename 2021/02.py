
from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

fin = (Path(__file__).parent / "in/02.in").open().read()
commands = fin.split('\n')
commands = [command.split(' ') for command in commands]
commands = [(x, int(y)) for x, y in commands] #cast the types

################ Common Function #################

################ Part 1 #################

h_pos = 0
depth = 0

for command in commands:
    action, qty = command
    if action == 'forward':
        h_pos += qty
    elif action == 'down':
        depth += qty
    elif action == 'up':
        depth -= qty

print('ans1:',h_pos * depth)

################ Part 2 #################

h_pos = 0
depth = 0
aim = 0

for command in commands:
    action, qty = command
    if action == 'forward':
        h_pos += qty
        depth += aim * qty
    elif action == 'down':
        aim += qty
    elif action == 'up':
        aim -= qty

print('ans2:',h_pos * depth)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))