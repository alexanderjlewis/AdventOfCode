from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

fin = (Path(__file__).parent / "in/test/10.in") #(ANS1=13140,ANS2=)
fin = (Path(__file__).parent / "in/10.in")

instructions = []
with open(fin, "r") as f:
    instructions = f.read().split("\n")
    

################ Common Function #################

def increment_cycle(cycle,qty,x):

    for _ in range(qty):
        cycle += 1
        if (cycle == 20) or ( (cycle > 20) and (cycle - 20) % 40 == 0):
            signal_strenghts.append(cycle * x)

    return cycle

def increment_cycle_and_crt(cycle,qty,x,crt):

    for _ in range(qty):
        cycle += 1
        crt_x = (len(crt) % 40)
        if crt_x in range(x-1,x+2):
            crt.append("#")
        else:
            crt.append(' ')

    return cycle, crt

def output_crt(crt):
    for y in range(6):
        print(''.join(crt[(y*40):(y+1)*40]))

################ Part 1 #################

cycle = 0
x = 1
signal_strenghts = []

for instruction in instructions:
    if instruction == "noop":
        cycle = increment_cycle(cycle,1,x)
    else:
        _,value = instruction.split(' ')
        cycle = increment_cycle(cycle,2,x)
        x += int(value)

print('ans1:',sum(signal_strenghts))

################ Part 2 #################

crt = []
cycle = 0
x = 1

for instruction in instructions:
    if instruction == "noop":
        cycle, crt = increment_cycle_and_crt(cycle,1,x,crt)
    else:
        _,value = instruction.split(' ')
        cycle, crt = increment_cycle_and_crt(cycle,2,x,crt)
        x += int(value)

print('ans2:')
output_crt(crt)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))