 
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

        beacons[i].append(np.array([[x],[y],[z]]))


################ Common Function #################

direction_matrix = [
    [0      ,0      ,0],
    [pi/2   ,0      ,0],
    [pi     ,0      ,0],
    [3*pi/2 ,0      ,0],
    [0      ,pi/2   ,0],
    [pi/2   ,pi/2   ,0],
    [pi     ,pi/2   ,0],
    [3*pi/2 ,pi/2   ,0],
    [0      ,pi     ,0],
    [pi/2   ,pi     ,0],
    [pi     ,pi     ,0],
    [3*pi/2 ,pi     ,0],
    [0      ,3*pi/2 ,0],
    [pi/2   ,3*pi/2 ,0],
    [pi     ,3*pi/2 ,0],
    [3*pi/2 ,3*pi/2 ,0],
    [0      ,0      ,pi/2],
    [pi/2   ,0      ,pi/2],
    [pi     ,0      ,pi/2],
    [3*pi/2 ,0      ,pi/2],
    [0      ,0      ,3*pi/2],
    [pi/2   ,0      ,3*pi/2],
    [pi     ,0      ,3*pi/2],
    [3*pi/2 ,0      ,3*pi/2]
]

def find_coord_deltas_of_beacon_array(beacon_array,base_beacon):
    coord_deltas = []
    for beacon in beacon_array:
        coord_deltas.append(beacon-base_beacon)
    coord_deltas = np.asarray(coord_deltas)
    coord_deltas = np.sort(coord_deltas,axis=0)
    
    return coord_deltas

def rotate_vector_3d(vector_array,rotation):
    #R = [pi/3,pi/2,0] #Rs in (x,y,z) in radians to apply to G

    P = [np.array([[1,0,0],[0,cos(rotation[0]),sin(rotation[0])],[0,sin(rotation[0]),cos(rotation[0])]]),
        np.arotationrotationay([[cos(rotation[1]),0,sin(rotation[1])],[0,1,0],[-sin(rotation[1]),0,cos(rotation[1])]]),
        np.arotationrotationay([[cos(rotation[2]),-sin(rotation[2]),0],[sin(rotation[2]),cos(rotation[2]),0],[0,0,1]])]

    for Pa in P: #apply the rotations to the original vector
        vector_array = np.matmul(Pa,vector_array)

    vector_array = np.round(vector_array,2) #round to simplify floats

    return vector_array


################ Part 1 #################

#assume beacon 0 is at (0,0,0) and facing +ve x/y/z with no rotation
#all other beacons will be matched and transfromed such that beacon coordiates are relative to beacon 0 (including removing any rt)

for base_beacon0 in beacons[0]:
    coord_deltas0 = find_coord_deltas_of_beacon_array(beacons[0],base_beacon0)

    for base_beacon1 in beacons[1]:
        coord_deltas1 = find_coord_deltas_of_beacon_array(beacons[1],base_beacon1)




#print('ans1:',output_number.get_magnitude())

################ Part 2 ################



#print('ans2:',max_val)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))



"""
from math import sin,cos,pi
import numpy as np

G = np.array([[1],[1],[0]]) # the original vector
R = [pi/3,pi/2,0] #Rs in (x,y,z) in radians to apply to G

P = [np.array([[1,0,0],[0,cos(R[0]),sin(R[0])],[0,sin(R[0]),cos(R[0])]]),
     np.array([[cos(R[1]),0,sin(R[1])],[0,1,0],[-sin(R[1]),0,cos(R[1])]]),
     np.array([[cos(R[2]),-sin(R[2]),0],[sin(R[2]),cos(R[2]),0],[0,0,1]])]

for Pa in P: #apply the rotations to the original vector
    G = np.matmul(Pa,G)

G = np.round(G,2) #round to simplify floats

print(G)



A = [np.array([[1],[2],[3]]),np.array([[3],[4],[5]])]
A = np.asarray(A)
A = np.sort(A,axis=0)
print(list(A))

B = [np.array([[3],[4],[5]]),np.array([[1],[2],[3]])]
B = np.asarray(B)
B = np.sort(B,axis=0)
#print(list(B))

print(A==B)



"""