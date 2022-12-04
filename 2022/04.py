from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

fin = (Path(__file__).parent / "in/test/04.in") #(ANS1=2,ANS2=4)
fin = (Path(__file__).parent / "in/04.in")

sections = []
with open(fin, "r") as f:
    data = f.read()   
    for line in data.split("\n"):
        a,b = line.split(",")
        al,au = a.split("-")
        bl,bu = b.split("-")
        sections.append([(int(al),int(au)),(int(bl),int(bu))]) 

################ Common Function #################



################ Part 1 #################

overlaps = 0

for row in sections:
    a,b = row
    al,au = a
    bl,bu = b

    if bl>=al and bu<=au:
        overlaps += 1
    elif al>=bl and au<=bu:
       overlaps += 1

print('ans1:',overlaps)

################ Part 2 #################

overlaps = 0

for row in sections:
    a,b = row
    al,au = a
    bl,bu = b

    if bl>au or al>bu:
        pass
    else:
        overlaps += 1

print('ans2:',overlaps)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))