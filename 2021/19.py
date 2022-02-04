
from copy import deepcopy
from pathlib import Path
from time import time
from math import ceil, floor
from itertools import combinations

t0 = time()

################ Data Processing #################

points = []
instructions = []

fin = (Path(__file__).parent / "in/test/19.in") #(ANS1=79,ANS2=)
#fin = (Path(__file__).parent / "in/19.in")
with open(fin, "r") as f:
    data = f.read()
    data = data.split('\n\n')
    data = [x.splitlines() for x in data]

beacons = {}
deltas = {}

#print(data)

for i,entry in enumerate(data):
    data = entry[1:]
    beacons[i] = []
    for beacon in data:
        x,y,z = beacon.split(',')
        x,y,z = int(x), int(y), int(z),

        beacons[i].append((x,y,z))

def find_overlapping_beacons(beacon_ids):
    scanner1 = deepcopy(beacons[beacon_ids[0]])
    scanner2 = deepcopy(beacons[beacon_ids[1]])

    for l1 in range(len(scanner1)):
        deltas1 = []
        abs_deltas1 = []
        base1 = scanner1[l1]
        for entry in scanner1:
            res = tuple(map(lambda i, j: (i - j), entry, base1))
            deltas1.append(res)
            abs_res = tuple(map(lambda i, j: abs(i - j), entry, base1))
            abs_deltas1.append(sorted(abs_res))

        for l2 in range(len(scanner2)):
            base2 = scanner2[l2]
            deltas2 = []
            abs_deltas2 = []
            for entry in scanner2:
                res = tuple(map(lambda i, j: (i - j), entry, base2))
                deltas2.append(res)
                abs_res = tuple(map(lambda i, j: abs(i - j), entry, base2))
                abs_deltas2.append(sorted(abs_res))

            matches = []
            abs_matches = []
            for i, delta2 in enumerate(abs_deltas2):
                for j, delta1 in enumerate(abs_deltas1):
                    if delta1 == delta2:
                        matches.append((scanner2[i],scanner1[j]))
                        abs_matches.append((deltas2[i],deltas1[j]))
            
            if len(matches) == 12:
                break
        
        if len(matches) == 12:
                break
        
    if len(matches) >= 12:
        abs_matches.remove(((0, 0, 0), (0, 0, 0)))
        print(matches)
        print(abs_matches)
        
        # now we need to calculate the offset and roation transformation required to get things into reference with beacon 0.
        a,b = abs_matches[0]
        transfroms = {}
        
        if abs(a[0]) == abs(b[0]):
            sign = int(b[0]/a[0])
            transfroms['x'] = (sign,0,0)
        elif abs(a[0]) == abs(b[1]):
            sign = int(b[1]/a[0])
            transfroms['x'] = (0,sign,0)
        elif abs(a[0]) == abs(b[2]):
            sign = int(b[2]/a[0])
            transfroms['x'] = (0,0,sign)
        
        if abs(a[1]) == abs(b[0]):
            sign = int(b[0]/a[1])
            transfroms['y'] = (sign,0,0)
        elif abs(a[1]) == abs(b[1]):
            sign = int(b[1]/a[1])
            transfroms['y'] = (0,sign,0)
        elif abs(a[1]) == abs(b[2]):
            sign = int(b[2]/a[1])
            transfroms['y'] = (0,0,sign)

        if abs(a[2]) == abs(b[0]):
            sign = int(b[0]/a[2])
            transfroms['z'] = (sign,0,0)
        elif abs(a[2]) == abs(b[1]):
            sign = int(b[1]/a[2])
            transfroms['z'] = (0,sign,0)
        elif abs(a[2]) == abs(b[2]):
            sign = int(b[2]/a[2])
            transfroms['z'] = (0,0,sign)

        x1,y1,z1 = base1
        x2,y2,z2 = base2
        offset = x1+x2,y1-y2,z1+z2
        print(offset)
        print(transfroms)





        return 'count pass'


        '''print(scanner1,scanner2)
        
        print(deltas1)
        print(deltas2)'''

        

    else:
        return 'count fail'


#print(beacons)

################ Common Function #################


################ Part 1 #################

beacon_list = list(range(1,len(beacons)))
print(beacon_list)

for beacon in beacon_list:
    pair = (1,beacon)
    print(pair,find_overlapping_beacons(pair))

#print('ans1:',output_number.get_magnitude())

################ Part 2 ################



#print('ans2:',max_val)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))