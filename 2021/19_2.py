<<<<<<< HEAD

from copy import deepcopy as dc
from pathlib import Path
=======
 
from itertools import product
from pathlib import Path
from time import time
from math import ceil, floor, sin, cos, pi
import numpy as np
>>>>>>> 5bac1b0faf107b591862e39cde6eb7f5c15d099f


fin = (Path(__file__).parent / "in/19.in")

scanners = []

<<<<<<< HEAD
=======
#fin = (Path(__file__).parent / "in/test/19.in") #(ANS1=79,ANS2=)
fin = (Path(__file__).parent / "in/19.in")
>>>>>>> 5bac1b0faf107b591862e39cde6eb7f5c15d099f
with open(fin, "r") as f:
    data = f.read()   
    for s in data.split("\n\n"):
        s = s.splitlines()[1:]
        scanners.append({tuple(map(int, k.split(","))) for k in s})

def rotations(s):
    s = dc(s)
    k = []
    for _ in range(4):
        for _ in range(4):
            k.append(s)
            s = {(z, y, -x) for x, y, z in s}
        k.append({(y, -x, z) for x, y, z in s})
        k.append({(-y, x, z) for x, y, z in s})
        s = {(x, z, -y) for x, y, z in s}
    return k

<<<<<<< HEAD
def vinv(x):
    return tuple(-k for k in x)

def vadd(x, y):
    return tuple(a + b for a, b in zip(x, y))
=======
for i,entry in enumerate(data):
    data = entry[1:]
    beacons[i] = []
    for beacon in data:
        x,y,z = beacon.split(',')
        x,y,z = int(x), int(y), int(z),
>>>>>>> 5bac1b0faf107b591862e39cde6eb7f5c15d099f

def vsub(x, y):
    return tuple(a - b for a, b in zip(x, y))

def calc_intersect(s1, s2):
    for s2 in rotations(s2):
        for a in s1:
            for b in s2:
                off = vsub(b, a)
                c = {vsub(b, off) for b in s2}
                if len(s1 & c) >= 12:
                    return c

t = set(scanners[0])

<<<<<<< HEAD
q = scanners[1:]

while q:
    k = calc_intersect(t, q[0])
    if k:
        t |= k
        q.pop(0)
    else:
        q.append(q.pop(0))

print(len(t))
=======
directions_matrix = [
    [0      ,0      ,0],     [pi/2   ,0      ,0],   [pi     ,0      ,0],     [3*pi/2 ,0      ,0],
    [0      ,pi/2   ,0],     [pi/2   ,pi/2   ,0],   [pi     ,pi/2   ,0],     [3*pi/2 ,pi/2   ,0],
    [0      ,pi     ,0],     [pi/2   ,pi     ,0],   [pi     ,pi     ,0],     [3*pi/2 ,pi     ,0],
    [0      ,3*pi/2 ,0],     [pi/2   ,3*pi/2 ,0],   [pi     ,3*pi/2 ,0],     [3*pi/2 ,3*pi/2 ,0],
    [0      ,0      ,pi/2],  [pi/2   ,0      ,pi/2],[pi     ,0      ,pi/2],  [3*pi/2 ,0      ,pi/2],
    [0      ,0      ,3*pi/2],[pi/2   ,0    ,3*pi/2],[pi     ,0      ,3*pi/2],[3*pi/2 ,0      ,3*pi/2]
]

def calc_deltas_between_beacons_in_array(beacon_array,base_beacon):
    deltas = []
    for beacon in beacon_array:
        deltas.append(beacon - base_beacon)
    deltas = np.asarray(deltas)
    return deltas


def rotate_vector_3d(vector,rotation):
    
    P = [np.array([[1,0,0],[0,cos(rotation[0]),-sin(rotation[0])],[0,sin(rotation[0]),cos(rotation[0])]]),
        np.array([[cos(rotation[1]),0,sin(rotation[1])],[0,1,0],[-sin(rotation[1]),0,cos(rotation[1])]]),
        np.array([[cos(rotation[2]),-sin(rotation[2]),0],[sin(rotation[2]),cos(rotation[2]),0],[0,0,1]])]

    for Pa in P: #apply the rotations to the original vector
        vector = np.matmul(Pa,vector)

    vector = np.round(vector,2) #round to simplify floats

    return vector


def rotate_and_compare(beacon_pair,base_array,comparison_array):

    for direction in directions_matrix:
        
        comparison_array_rotated_and_offset = []

        for entry in comparison_array:
            comparison_array_rotated_and_offset.append(rotate_vector_3d(entry,direction))
    
        offset = beacon_pair[0] - rotate_vector_3d(beacon_pair[1],direction)

        for i, _ in enumerate(comparison_array_rotated_and_offset):
            comparison_array_rotated_and_offset[i] += offset

        matches = 0
        unmatched_beacons = []

        for comparison_array_beacon in comparison_array_rotated_and_offset:

            if np.any(np.all(comparison_array_beacon == base_array, axis=1)):
                matches += 1
            else:
                unmatched_beacons.append(comparison_array_beacon)
        
        if matches >= 12:
                       
            return True, unmatched_beacons

    return False, None


################ Part 1 #################

#assume beacon 0 is at (0,0,0) and facing +ve x/y/z with no rotation
#all other beacons will be matched and transfromed such that beacon coordiates are relative to beacon 0 (including removing any rt)

beacons_to_parse = list(range(1,len(beacons)))

i = 0

while len(beacons_to_parse) > 0:

    if i >= len(beacons_to_parse):
        i = 0

    for beacon_pair in product(beacons[0],beacons[beacons_to_parse[i]]):
               
        match, unmatched_beacons = rotate_and_compare(beacon_pair,beacons[0],beacons[beacons_to_parse[i]])
        
        if match:

            print('matched 0 and ',beacons_to_parse[i])

            beacons_to_parse.pop(i)
            
            beacons[0].extend(unmatched_beacons)
            
            break

    i += 1

print('ans1:',len(beacons[0]))

################ Part 2 ################



#print('ans2:',max_val)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))



"""



"""z
>>>>>>> 5bac1b0faf107b591862e39cde6eb7f5c15d099f
