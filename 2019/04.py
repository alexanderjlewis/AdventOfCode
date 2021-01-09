from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

a,b = (Path(__file__).parent / "in/04.in").open().read().split('-')
low = int(a)
high = int(b)

################ Part 1 #################

out1 = []
for c in range(low,high):
    b = list(str(c))
    if sorted(b) == b and any((b[i] == b[i-1]) for i in range(1,len(b))): 
        out1.append(c)

print('ans1:',len(out1))

################ Part 2 #################
# Not a clean solution for part 2....

out2 = []

for j in out1:
    chars = [str(x) for x in list(str(j))]
    temp = None
    for char in chars:
        if not temp:
            temp = char
        else:
            if char == temp[0]:
                temp += char
            else:
                if len(temp) == 2:
                    out2.append(j)
                    temp = ''
                    break
                else:
                    temp = char
    if len(temp) == 2:
        out2.append(j)

print('ans2:',len(out2))

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))