from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

lines = (Path(__file__).parent / "in/06.in").open().readlines()
data = {}
for line in lines:
    a, b = line.split(')')
    b = b.replace('\n','')
    if a in data:
        data[a].append(b)
    else:
        data[a] = [b]


#print(data)

################ Part 1 #################

def orbits(a,i):
    count = 0
    if a in data:
        orbitting = data[a]
        #print(orbitting,'orbitting',a)
        for item in orbitting:
            count += orbits(item,i+1)
        return count + i
    else:
        #print('nothing orbitting',a,'returning',i+1)
        return i

print('ans1:',orbits('COM',0))

################ Part 2 #################

def path(a,g):
    if a[-1] == g:
        return a
    elif a[-1] in data:
        orbitting = data[a[-1]]
        for item in orbitting:
            c = a[:]
            c.append(item)
            d = path(c,g)
            if d:
                return d
    return None

route1 = path(['COM'],'YOU')
route2 = path(['COM'],'SAN')

i = 0
while True:
    if route2[i] != route1[i]:
        break
    i += 1

print('ans2:',len(route1) + len(route2) - (2*i) - 2)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))