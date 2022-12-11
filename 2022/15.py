from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

fin = (Path(__file__).parent / "in/test/15.in") #(ANS1=,ANS2=)
#fin = (Path(__file__).parent / "in/15.in")

values = []
with open(fin, "r") as f:
    data = f.read()   
    

################ Common Function #################



################ Part 1 #################



print('ans1:',)

################ Part 2 #################



print('ans2:',)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))