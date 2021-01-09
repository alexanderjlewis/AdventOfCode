from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

lines = (Path(__file__).parent / "in/05.in").open().read().split(',')
instructions = list(map(int,lines))

################ Part 1 #################

def mode(d,i,p1,p2):
    try:
        if p1 == 0:
            t1 = d[d[i+1]]
        else:
            t1 = d[i+1]
        if p2 == 0:
            t2 = d[d[i+2]]
        else:
            t2 = d[i+2]
    except:
        t1 = None
        t2 = None
    return t1,t2

def process(d,a):
    i = 0
    out = []
    while i < len(d):
        d_in = str(d[i]).rjust(5,'0')
        opcode = d_in[3:]
        p1 = int(d_in[2])
        p2 = int(d_in[1])
        t1, t2 = mode(d,i,p1,p2)
        if opcode == '01':
            d[d[i+3]] = t1 + t2
            i += 4
        elif opcode == '02':
            d[d[i+3]] = t1 * t2
            i += 4
        elif opcode == '03':
            d[d[i+1]] = a
            i += 2
        elif opcode == '04':
            if p1 == 0:
                out.append(d[d[i+1]])
            else:
                out.append(d[i+1])
            i += 2
        elif opcode == '05':
            if t1 != 0:
                i = t2
            else:
                i += 3
        elif opcode == '06':
            if t1 == 0:
                i = t2
            else:
                i += 3
        elif opcode == '07':
            d[d[i+3]] = 1 if t1 < t2 else 0
            i += 4
        elif opcode == '08':
            d[d[i+3]] = 1 if t1 == t2 else 0
            i += 4
        else: 
            break
    return out

print('ans1:',process(instructions[:],1)[-1])

################ Part 2 #################

print('ans2:',process(instructions[:],5)[0])

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))
