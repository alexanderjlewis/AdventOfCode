
from pathlib import Path
from time import time
from types import SimpleNamespace

t0 = time()

################ Data Processing #################

signal_list = []
output_list = []

fin = (Path(__file__).parent / "in/08_test.in")
#fin = (Path(__file__).parent / "in/08.in")
with open(fin, "r") as f:
    
    for line in f:
        signal,output = line.strip().split(' | ')
        signal_list.append(signal.split(' '))
        output_list.append(output.split(' '))

################ Common Function #################



################ Part 1 #################

lengths = [2,3,4,7]

count = 0

for outputs in output_list:
    for output in outputs:
        if len(output) in lengths:
            count += 1

print('ans1:',count)

################ Part 2 ################



# '4' Digit plus Segment 'A' + Segment ? - find the only one with a single difference, that's the 9 and Segment 'G'
# Only missing Segment from 9 digit is 'E'
# '3' Digit + Segment 'A' + 'G' + Segment ? - find the only one with a single difference, that's the 3 and Segment 'D'
# Difference between digits 3 and 9 gives Segment 'B'
# '5' Digit minus Segments A/B/D/G gives 'F'
# '1' Digit minus Segment F gives 'C'
# 
# 
# 

A = int('1000000',2)
B = int('0100000',2)
C = int('0010000',2)
D = int('0001000',2)
E = int('0000100',2)
F = int('0000010',2)
G = int('0000001',2)

print(bin(A&B))

segments = {'A':'','B':'','C':'','D':'','E':'','F':'','G':'',}

numbers = {0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}

signals = signal_list[0]

for i in range(len(signals)-1,-1,-1):
    if len(signals[i]) == 2:
        numbers[1] = signals[i]
        signals.pop(i)
    elif len(signals[i]) == 3:
        numbers[7] = signals[i]
        signals.pop(i)
    elif len(signals[i]) == 4:
        numbers[4] = signals[i]
        signals.pop(i)
    elif len(signals[i]) == 7:
        numbers[8] = signals[i]
        signals.pop(i)

signals = [''.join(sorted(signal)) for signal in signals]
print(signals)

#### Rule 1 ####
# Segment 'A' is difference between the 7 and 1 digits

segments['A'] = numbers[7]

for char in numbers[1]:
    segments['A'] = segments['A'].replace(char,'')

#### Rule 2 ####


numbers[9] = numbers[4] + segments['A']

#for char in numbers[1]:
#    segments['A'] = segments['A'].replace(char,'')

########

print(numbers)
print(segments)


#print('ans2:',min(fuel))

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))