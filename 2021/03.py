
from pathlib import Path
from time import time
from copy import deepcopy

t0 = time()

################ Data Processing #################

#fin = (Path(__file__).parent / "in/test/03.in") #(ANS1=4512,ANS2=1924)
fin = (Path(__file__).parent / "in/03.in")
with open(fin, "r") as f:
    numbers = [list(line.replace('\n','')) for line in f]
    numbers = [[int(digit) for digit in number] for number in numbers]

################ Common Function #################



################ Part 1 #################

numbers_length = len(numbers)
number_columns = list(zip(*numbers))
column_sums = [sum(column) for column in number_columns]

gamma_rate = ''
epsilon_rate = ''

for column_sum in column_sums:
    if column_sum > numbers_length/2:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

gamma_rate = int(gamma_rate,2)
epsilon_rate = int(epsilon_rate,2)

print('ans1:',gamma_rate * epsilon_rate)

################ Part 2 #################

o2_rate = ''
oxygen_rate = ''

numbers_o2_gen = deepcopy(numbers)
numbers_oxy_rate = deepcopy(numbers)

bit_pos = 0

while len(numbers_o2_gen) > 1:

    o2_gen_columns = list(zip(*numbers_o2_gen))
    o2_gen_sums = [sum(column) for column in o2_gen_columns]
 
    if o2_gen_sums[bit_pos] >= len(numbers_o2_gen)/2:
        numbers_o2_gen[:] = (x for x in numbers_o2_gen if x[bit_pos] == 1)
    else:
        numbers_o2_gen[:] = (x for x in numbers_o2_gen if x[bit_pos] == 0)

    bit_pos += 1

bit_pos = 0

while len(numbers_oxy_rate) > 1:

    oxy_rate_columns = list(zip(*numbers_oxy_rate))
    oxy_sums = [sum(column) for column in oxy_rate_columns]

    if oxy_sums[bit_pos] >= len(numbers_oxy_rate)/2:
        numbers_oxy_rate[:] = (x for x in numbers_oxy_rate if x[bit_pos] == 0)
    else:
        numbers_oxy_rate[:] = (x for x in numbers_oxy_rate if x[bit_pos] == 1)

    bit_pos += 1

o2_rate = ''.join(map(str,numbers_o2_gen[0]))
oxygen_rate = ''.join(map(str,numbers_oxy_rate[0]))

o2_rate = int(o2_rate,2)
oxygen_rate = int(oxygen_rate,2)

print('ans2:',o2_rate * oxygen_rate)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))