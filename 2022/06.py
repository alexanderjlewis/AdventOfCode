from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

#fin = (Path(__file__).parent / "in/test/06.in") #(ANS1=7,ANS2=19)
fin = (Path(__file__).parent / "in/06.in")

datastream = []
with open(fin, "r") as f:
    datastream = (f.read())
    

################ Common Function #################

def find_start(datastream,n):
    counter = n
    while True:

        start = list(datastream[:n])
        if len(set(start)) == n:
            return counter

        datastream = datastream[1:]
        counter += 1

################ Part 1 #################

print('ans1:',find_start(datastream,4))

################ Part 2 #################

print('ans2:',find_start(datastream,14))

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))