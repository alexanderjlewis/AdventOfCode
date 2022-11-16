 
from copy import deepcopy
from pathlib import Path
from time import time
from math import ceil, floor, sin, cos, pi
from itertools import combinations
import numpy as np

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

def find_overlapping_beacons(beacon_id1,beacon_id2):
    scanner1 = deepcopy(beacons[beacon_id1])
    scanner2 = deepcopy(beacons[beacon_id2])

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
        
        print(matches)
        print(abs_matches)
        abs_matches.remove(((0, 0, 0), (0, 0, 0)))
        
        # now we need to calculate the offset and roation transformation required to get things into reference with beacon 0.
        a,b = abs_matches[0]
        transforms = {}
        signs = []
        
        if abs(a[0]) == abs(b[0]):
            sign = int(b[0]/a[0])
            transforms['x'] = [sign,0,0]
        elif abs(a[0]) == abs(b[1]):
            sign = int(b[1]/a[0])
            transforms['x'] = [0,sign,0]
        elif abs(a[0]) == abs(b[2]):
            sign = int(b[2]/a[0])
            transforms['x'] = [0,0,sign]
        signs.append(sign)
        
        if abs(a[1]) == abs(b[0]):
            sign = int(b[0]/a[1])
            transforms['y'] = [sign,0,0]
        elif abs(a[1]) == abs(b[1]):
            sign = int(b[1]/a[1])
            transforms['y'] = [0,sign,0]
        elif abs(a[1]) == abs(b[2]):
            sign = int(b[2]/a[1])
            transforms['y'] = [0,0,sign]
        signs.append(sign)

        if abs(a[2]) == abs(b[0]):
            sign = int(b[0]/a[2])
            transforms['z'] = [sign,0,0]
        elif abs(a[2]) == abs(b[1]):
            sign = int(b[1]/a[2])
            transforms['z'] = [0,sign,0]
        elif abs(a[2]) == abs(b[2]):
            sign = int(b[2]/a[2])
            transforms['z'] = [0,0,sign]
        signs.append(sign)

        x1,y1,z1 = matches[0][1]
 
        print(transforms)
        print(signs)
        print(x1,y1,z1)

        offset_x = sum(map(lambda i, j: (i * j), transforms['x'], list(matches[0][0])))
        offset_y = sum(map(lambda i, j: (i * j), transforms['y'], list(matches[0][0])))
        offset_z = sum(map(lambda i, j: (i * j), transforms['z'], list(matches[0][0])))

        print(offset_x,offset_y,offset_z)

        offset = x1-offset_x, y1-offset_y, z1-offset_z

        return True, offset, signs        

    else:
        return False, (), {}


#print(beacons)

################ Common Function #################


################ Part 1 #################

beacon_list = list(range(0,len(beacons)))
beacon_pairs = combinations(beacon_list,2)


success, offset, signs = find_overlapping_beacons(0,1)

print(offset)
print(signs)

offset_beacons = []

x_dir,y_dir,z_dir = signs
x_off,y_off,z_off = offset

for beacon in beacons[1]:
    x_mag,y_mag,z_mag = beacon
    
    offset_beacons.append((  (x_mag * x_dir) + x_off,
                            (y_mag * y_dir) + y_off,
                            (z_mag * z_dir) + z_off))


beacons[0].extend(offset_beacons)
beacons[0] = [*set(beacons[0])]

success, offset, signs = find_overlapping_beacons(0,4)

print(offset)
print(signs)



""" for pair in beacon_pairs:
    if find_overlapping_beacons(pair): 
        print(pair)
 """
#print('ans1:',output_number.get_magnitude())

################ Part 2 ################



#print('ans2:',max_val)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))