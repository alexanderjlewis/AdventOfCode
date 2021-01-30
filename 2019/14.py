from pathlib import Path
from time import time
import math

t0 = time()

################ Data Processing #################

lines = (Path(__file__).parent / "in/14.in").open().readlines()
reactions = {}
for line in lines:
    a,b = line.strip().split(' => ')
    b1,b2 = b.split(' ')
    temp = [int(b1)]
    for c in a.split(', '):
        c1,c2 = c.split(' ')
        temp.append([int(c1),c2])
    reactions[b2] = temp

print(reactions)

################ Part 1 #################

ore = 0

ingredients = reactions['FUEL']
ingredients.pop(0) #remove the first '1' associated with 'fuel'.

while len(ingredients) > 0:
    #print('b ingred',ingredients)
    next_quantity, next_item = ingredients.pop(0)
    if next_item == 'ORE':
        ore += next_quantity
        #print('ore found')
        continue

    #print('a ingred',ingredients)
    #print('next item',next_item)
    #print('react',reactions)
    next_items = reactions[next_item].copy()
    
    #print(next_quantity,next_items)
    next_ratio = math.ceil(next_quantity / next_items.pop(0))
    
    for i, item in enumerate(next_items):
        next_items[i][0] *= next_ratio
        ingredients.append(next_items[i])

    #print(next_ratio, next_items)
    #print(ingredients)

print('ans1:',ore)

################ Part 2 #################

print('ans2:','')

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))