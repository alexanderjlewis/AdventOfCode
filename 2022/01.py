from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

#fin = (Path(__file__).parent / "in/test/01.in") #(ANS1=24000,ANS2=)
fin = (Path(__file__).parent / "in/01.in")

elves = []
with open(fin, "r") as f:
    data = f.read()   
    for record in data.split("\n\n"):
        elves.append([int(line) for line in record.splitlines()])

################ Common Function #################

################ Part 1 #################

calories_pef_elf = [sum(elf) for elf in elves]
print('ans1:',max(calories_pef_elf))

################ Part 2 #################

calories_pef_elf = sorted(calories_pef_elf)
print('ans2:',sum(calories_pef_elf[-3:]))

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))