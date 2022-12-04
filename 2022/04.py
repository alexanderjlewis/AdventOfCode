from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

#fin = (Path(__file__).parent / "in/test/04.in") #(ANS1=2,ANS2=4)
fin = (Path(__file__).parent / "in/04.in")

sections = []
with open(fin, "r") as f:
    data = f.read()   
    for line in data.split("\n"):
        sections.append(list(map(int,line.replace('-',',').split(','))))

################ Common Function #################

################ Part 1 #################

overlaps_1 = 0
overlaps_2 = 0

for row in sections:
    s1, e1, s2, e2 = row

    r1 = set(range(s1,e1+1))
    r2 = set(range(s2,e2+1))

    if r1.issubset(r2) or r2.issubset(r1):
        overlaps_1 += 1

    if r1.intersection(r2):
        overlaps_2 += 1

print('ans1:',overlaps_1)

################ Part 2 #################

print('ans2:',overlaps_2)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))