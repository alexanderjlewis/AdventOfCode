from pathlib import Path
from time import time

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

with open(fin, "r") as f:
    data = f.read()
    for x in replace:
        data = data.replace(x,',')
    data = data.split("\n")
    
    for line in data:
        _,a,b,*c = line.split(',')
        instr[a] = (int(b),c)

non_zero_flow = []

for inst in instr:
    flow,tunnels = instr[inst]
    if flow > 0:
        non_zero_flow.append(inst)

################ Common Function #################

print(non_zero_flow)

    

################ Part 1 #################

max_pressure_released = []
queue = {}

start = 'AA'

def simulate(t,pos,pressure_released,opened):
    print('t',t)
    if t > 30:
        max_pressure_released.append(pressure_released)
        print(pressure_released)
        return


    flow, tunnels = instr[pos]
    t += 1

    for tunnel in tunnels:
        print('sim',tunnel)
        simulate(t,tunnel,pressure_released,opened)
        

        return

        
    if flow > 0 and pos not in opened:
        t += 1
        pressure_released += ( flow * (30 - t))
        opened.append(pos)
    
    for tunnel in tunnels:
        simulate(t,tunnel,pressure_released,opened)

simulate(0,start,0,[])

print('ans1:',max(max_pressure_released))

################ Part 2 #################



print('ans2:',)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))