from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

lines = (Path(__file__).parent / "in/02.in").open().readlines()

valid_count1 = 0
valid_count2 = 0

################ Common Function #################

for entry in lines:
    s, password = entry.split(": ")
    s, letter = s.split(' ')
    lower,upper = s.split('-')

    lower = int(lower)
    upper = int(upper)

    char_count = password.count(letter)

    ################ Part 1 #################
    if (upper >= char_count) and (lower <= char_count):
        valid_count1 += 1

    ################ Part 2 #################
    if (password[lower - 1] == letter) ^ (password[upper - 1] == letter):
        valid_count2 += 1

print('ans1:',valid_count1)
print('ans2:',valid_count2)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))