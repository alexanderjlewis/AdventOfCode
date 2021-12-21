
from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

fish_list = []

fin = (Path(__file__).parent / "in/06_test.in")
with open(fin, "r") as f:
   fish_list = f.read().split(',')
   fish_list = [int(x) for x in fish_list]

################ Common Function #################

def sim_fish(day_number,day_limit):
    #print('new fish:',day_number)
    
    number_fish = 1

    #print('next day_number:',day_number)

    if day_number > day_limit:
        pass
    else:
        while day_number <= day_limit:
            #print('rec - day:',day_number)
            number_fish += sim_fish(day_number + 9,day_limit)
            day_number += 7

    #print('returning fish',number_fish)
    return number_fish

################ Part 1 #################

options = [1,2,3,4,5]
answers = {}

day_limit = 80

for option in options:
    answers[option] = sim_fish(option+1,day_limit)

ans1 = 0

for fish in fish_list:
    ans1 += answers[fish]

print('ans1:',ans1)

################ Part 2 ################

def sim_fish2(days_remaining):
    #print('new fish:',days_remaining)
    
    number_fish = 1
    days_remaining -= 9
    
    #print('next day_number:',day_number)

    if days_remaining <= 0:
        pass
    else:
        while days_remaining > 0:
            #print('rec - day:',day_number)
            #print('dr',days_remaining,'adding',outs[days_remaining-1])
            number_fish += outs[days_remaining-1]
            days_remaining -= 7

    #print('returning fish',number_fish)
    return number_fish

outs = []

days = 256
for i in range(1,days+1):
    outs.append(sim_fish2(i))
    
options = [1,2,3,4,5]
answers = {}

day_limit = 18

for option in options:
    temp = 0
    x = day_limit - option - 1

    while x > 0:
        temp += outs[x]
        x -= 7

    answers[option] = temp

ans2 = len(fish_list)

for fish in fish_list:
    print('adding',answers[fish])
    ans2 += answers[fish]

print('ans2:',ans2)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))