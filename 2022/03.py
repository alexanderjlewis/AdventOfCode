from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

#fin = (Path(__file__).parent / "in/test/03.in") #(ANS1=157,ANS2=70)
fin = (Path(__file__).parent / "in/03.in")

rucksacks = []
with open(fin, "r") as f:
    data = f.read()   
    for rucksack in data.split("\n"):
        n = len(rucksack)
        n = n//2
        rucksacks.append((set(rucksack[:n]),set(rucksack[n:])))

################ Common Function #################

def character_value(character):
    value = 0

    if character.isupper():
        value += ord(character) - 64 + 26
    else:
        value += ord(character) - 96

    return value

################ Part 1 #################

priority = 0

for rucksack in rucksacks:
    common_item = list(rucksack[0] & rucksack[1])[0]
    priority += character_value(common_item)

print('ans1:',priority)

################ Part 2 #################

priority = 0
i=0

while i < len(rucksacks):
    
    badge = set()

    badge = list((rucksacks[i][0].union(rucksacks[i][1])) &
            (rucksacks[i+1][0].union(rucksacks[i+1][1])) &
            (rucksacks[i+2][0].union(rucksacks[i+2][1])))
    
    priority += character_value(badge[0])

    i += 3

print('ans2:',priority)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))