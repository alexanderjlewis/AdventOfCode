from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

fin = (Path(__file__).parent / "in/test/19.in") #(ANS1=,ANS2=)
#fin = (Path(__file__).parent / "in/19.in")

replace = [
    'Blueprint ',
    ': Each ore robot costs ',
    ' ore. Each clay robot costs ',
    ' ore. Each obsidian robot costs ',
    ' ore and ',
    ' clay. Each geode robot costs ',
    ' ore and ',
    ' obsidian.' 
]

blueprints = []

with open(fin, "r") as f:
    data = f.read()
    for x in replace:
        data = data.replace(x,',')
    data = data.split("\n")
    
    for line in data:
        _,a,b,c,d,e,f,g,_ = line.split(",")
        blueprints.append([(int(b),0,0),(int(c),0,0),(int(d),int(e),0),(int(f),0,int(g))])

print(blueprints)

    

################ Common Function #################

def simulate(time,ore_bots,resources):
    
    #work out how to spend resources


    
    #now update resource counts    
    for j in range(0,len(ore_bots)):
        resources[j] += ore_bots[j]

################ Part 1 #################

minutes = 24



bot_costs = blueprints[0]

ore_bots = [1,0,0,0]

resources = [0,0,0,0]

simulate(1,bot_costs,ore_bots,resources)




print('ans1:',)

################ Part 2 #################



print('ans2:',)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))