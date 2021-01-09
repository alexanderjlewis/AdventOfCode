from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

lines = (Path(__file__).parent / "in/02.in").open().read().split(',')
d = list(map(int,lines))

################ Part 1 #################

def check_noun_verb(a,n,v):
    a = a[:]
    a[1] = n
    a[2] = v
    for i in range(0,len(a),4):
        if a[i] == 1:
            a[a[i+3]] = a[a[i+1]] + a[a[i+2]]
        elif d[i] == 2:
            a[a[i+3]] = a[a[i+1]] * a[a[i+2]]
        else:
            break
    return a[0]

print('ans1:',check_noun_verb(d,12,2))

################ Part 2 #################

for i in range(100):
    for j in range(100):
        print('ans2:',100*i+j) if check_noun_verb(d,i,j) == 19690720 else next

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))
