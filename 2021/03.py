
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

numbers_length = len(numbers)

print(numbers)

################ Part 1 #################

bits = zip(*numbers)
a = (list(map(list,bits)))
a = a[0]
print(max(set(a), key = a.count))
print(min(set(a), key = a.count))
bits = [sum(bit) for bit in bits]
print(bits)

gamma_rate = ''
epsilon_rate = ''

for bit in bits:
    if bit > numbers_length/2:
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

number_o2_gen = deepcopy(numbers)
number_oxy_rate = deepcopy(numbers)

bit_pos = 0

while len(number_o2_gen) > 1:

    bits = zip(*number_o2_gen)
    bits = [sum(bit) for bit in bits]

    if bits[bit_pos] >= len(number_o2_gen)/2:
        number_o2_gen[:] = (x for x in number_o2_gen if x[bit_pos] == 1)
    else:
        number_o2_gen[:] = (x for x in number_o2_gen if x[bit_pos] == 0)

    bit_pos += 1

bit_pos = 0

while len(number_oxy_rate) > 1:

    bits = zip(*number_oxy_rate)
    bits = [sum(bit) for bit in bits]

    if bits[bit_pos] >= len(number_oxy_rate)/2:
        number_oxy_rate[:] = (x for x in number_oxy_rate if x[bit_pos] == 0)
    else:
        number_oxy_rate[:] = (x for x in number_oxy_rate if x[bit_pos] == 1)

    bit_pos += 1

o2_rate = ''.join(map(str,number_o2_gen[0]))
oxygen_rate = ''.join(map(str,number_oxy_rate[0]))

o2_rate = int(o2_rate,2)
oxygen_rate = int(oxygen_rate,2)

print('ans2:',o2_rate * oxygen_rate)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))