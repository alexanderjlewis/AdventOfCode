from pathlib import Path
from time import time
from copy import deepcopy

t0 = time()

################ Data Processing #################

fin = (Path(__file__).parent / "in/test/13.in") #(ANS1=13,ANS2=140)
fin = (Path(__file__).parent / "in/13.in")

pairs = []
with open(fin, "r") as f:
    data = f.read().split("\n\n")
    for i,x in enumerate(data):
        a,b = x.split("\n")
        a = eval(a)
        b = eval(b)
        pairs.append([a,b])

################ Common Function #################

def compare_items(left,right):

    while True:
        
        l = None
        r = None

        if len(left) == 0 and len(right) == 0:
            return None
        if len(left) > 0:
            l = left.pop(0)
        else:
            return True

        if len(right) > 0:
            r = right.pop(0)
        else:
            return False

        if type(l) == int and type(r) == int:
            if l == r:
                next
            elif l < r:
                return True
            else:
                return False
        
        elif type(l) == list and type(r) == list:
            result = compare_items(l,r)
            if result == None:
                next
            else:
                return result

        elif type(l) == int:
            l = [l]
            result = compare_items(l,r)
            if result == None:
                next
            else:
                return result

        elif type(r) == int:
            r = [r]
            result = compare_items(l,r)
            if result == None:
                next
            else:
                return result

################ Part 1 #################

correct_indexes = []

pairs_1 = deepcopy(pairs)

for i in range(len(pairs_1)):

    left,right = pairs_1[i]

    if compare_items(left,right):
        correct_indexes.append(i+1)

print('ans1:',sum(correct_indexes))

################ Part 2 #################

lines = []
for a,b in pairs:
    lines.append(a)
    lines.append(b)

additional_vals = [[[2]],[[6]]]
lines.extend(additional_vals)

sorted_lines = []

for i in range(len(lines)):
    base_index = i

    for j in range(i+1,len(lines)):
        result = compare_items(deepcopy(lines[base_index]),deepcopy(lines[j]))
        if not result:
            base_index = j

    lines.insert(i,lines.pop(base_index))

a = lines.index([[2]]) + 1
b = lines.index([[6]]) + 1

print('ans2:', a * b)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))