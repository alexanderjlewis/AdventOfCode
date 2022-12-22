from pathlib import Path
from time import time
import itertools

t0 = time()

################ Data Processing #################

fin = (Path(__file__).parent / "in/test/16.in") #(ANS1=1651,ANS2=)
#fin = (Path(__file__).parent / "in/16.in")

replace = [
    'Valve ',
    ' has flow rate=',
    '; tunnels lead to valves ',
    '; tunnel leads to valve ',
    ', ',
]

instr = {}
non_zero_flows = []

with open(fin, "r") as f:
    data = f.read()
    for x in replace:
        data = data.replace(x,',')
    data = data.split("\n")
    
    for line in data:
        _,a,b,*c = line.split(',')
        instr[a] = (int(b),c)

        if int(b) > 0:
            non_zero_flows.append(a)
       

################ Common Function #################

print(non_zero_flows)

    

################ Part 1 #################

max_pressure_released = []
queue = {}

start = 'AA'


print('ans1:',max(max_pressure_released))

################ Part 2 #################



print('ans2:',)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))