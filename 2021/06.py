
from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

fish_list = []

fin = (Path(__file__).parent / "in/06.in")
with open(fin, "r") as f:
   fish_list = f.read().split(',')
   fish_list = [int(x) for x in fish_list]

#print(fish_list)

################ Common Function #################

def brute_force_fish(days,fish_list):
    new_fish = 0

    for _ in range(days):
        new_fish = 0
        for i, fish in enumerate(fish_list):
            if fish == 0:
                fish_list[i] = 6
                new_fish += 1
            else:
                fish_list[i] -= 1
        
        for i in range(new_fish):
            fish_list.append(8)
        
        #print(fish_list)

    return len(fish_list)

################ Part 1 #################

options = [1,2,3,4,5]
answers = {}

days = 80

for option in options:
    answers[option] = brute_force_fish(days,[option])

ans1 = 0

for fish in fish_list:
    ans1 += answers[fish]

print('ans1:',ans1)

################ Part 2 #################

options = [1]
answers = {}

days = 256

for option in options:
    answers[option] = brute_force_fish(days,[option])

ans2 = 0

for fish in fish_list:
    ans1 += answers[fish]

print('ans2:',ans2)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))