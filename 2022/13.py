from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

fin = (Path(__file__).parent / "in/test/13.in") #(ANS1=12,ANS2=)
#fin = (Path(__file__).parent / "in/13.in")

pairs = []
with open(fin, "r") as f:
    data = f.read().split("\n\n")
    for x in data:
        a,b = x.split("\n")
        a = eval(a)
        b = eval(b)
        pairs.append([a,b])

################ Common Function #################

def compare_items(l,r):
    if type(l) == int and type(r) == int:
        if l == r:
            left.pop(0)
            right.pop(0)
            print('l=r')
        elif l < r:
            correct_indexes.append(i+1)
            return True
        else:
            return False
    
    elif type(l) == list and type(r) == list:
        return False

    elif type(l) == int:
        l = [l]
        return False

    elif type(r) == int:
        r = [r]
        return False

################ Part 1 #################

correct_indexes = []

for i in range(len(pairs)):

    left,right = pairs[i]

    while True:     
        
        l = None
        r = None
        print(i)
        
        if len(left) > 0:
            l = left[0]
        else:
            correct_indexes.append(i+1)
            break

        if len(right) > 0:
            r = right[0]
        else:
            break
  
        result = compare_items(l,r)
        

        

        print(l,r)
    i += 1
        

print('corr:',correct_indexes)

print('ans1:',)

################ Part 2 #################



print('ans2:',)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))