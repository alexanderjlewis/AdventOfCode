from pathlib import Path
from time import time
from itertools import combinations

t0 = time()

################ Data Processing #################

lines = (Path(__file__).parent / "in/12.in").open().readlines()

lines = [line.replace('<','').strip().replace('>','').replace(' ','').split(',') for line in lines]

################ Part 1 #################

pos = []
vel = []

n = 1000

for line in lines:
    pos.append([int(line[0][2:]),int(line[1][2:]),int(line[2][2:])])
    vel.append([0]*3)

moon_combos = list(combinations(list(range(0,len(pos))),2))

for x in range(n):
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

print('ans1:',sum(sum(abs(x) for x in pos[i]) * sum(abs(x) for x in vel[i]) for i in range(len(pos))))

################ Part 2 #################


#print('ans2:')

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))