from pathlib import Path
from time import time
from itertools import combinations
from math import gcd
from functools import reduce
import copy

t0 = time()

################ Data Processing #################

lines = (Path(__file__).parent / "in/12.in").open().readlines()

lines = [line.replace('<','').strip().replace('>','').replace(' ','').split(',') for line in lines]

pos, vel = [], []

for line in lines:
    pos.append([int(line[0][2:]),int(line[1][2:]),int(line[2][2:])])
    vel.append([0]*3)

moon_combos = list(combinations(list(range(0,len(pos))),2))

################ Helper Functions #################

def lcm(denominators):
    return reduce(lambda a,b: a*b // gcd(a,b), denominators)

def simulate(pos,vel):
    for pair in moon_combos:
        a, b = pos[pair[0]], pos[pair[1]]
        for i in range(3):
            if a[i] > b[i]:
                vel[pair[0]][i] -= 1
                vel[pair[1]][i] += 1
            elif b[i] > a[i]:
                vel[pair[0]][i] += 1
                vel[pair[1]][i] -= 1    

    for i in range(len(pos)):
        pos[i] = [sum(x) for x in zip(pos[i], vel[i])]
    
    return pos, vel

################ Part 1 #################

n = 1000

pos1 = copy.deepcopy(pos)
vel1 = copy.deepcopy(vel)

for x in range(n):
    pos1, vel1 = simulate(pos1,vel1)

print('ans1:',sum(sum(abs(x) for x in pos1[i]) * sum(abs(x) for x in vel1[i]) for i in range(len(pos1))))

################ Part 2 #################

starting_positions = {}

for i in range(3):
    starting_positions[i] = [item[i] for item in pos]

counter = 1
loop_points = []

pos2 = copy.deepcopy(pos)
vel2 = copy.deepcopy(vel)

while True:
    pos2, vel2 = simulate(pos2,vel2)
    
    for j in range(3):
        if [item[j] for item in pos2] == starting_positions[j] and all(item[j] == 0 for item in vel2):
            loop_points.append(counter)
            
    if len(loop_points) == 3:
        break

    counter += 1

print('ans2:',lcm(loop_points))

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))