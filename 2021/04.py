
from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

fin = (Path(__file__).parent / "in/04_test.in").open().read()
commands = fin.split('\n')
commands = [command.split(' ') for command in commands]
commands = [(x, int(y)) for x, y in commands] #cast the types

################ Common Function #################



################ Part 1 #################


#print('ans1:',x)

################ Part 2 #################


#print('ans2:',y)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))