
from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

fish_starting_list = []

#fin = (Path(__file__).parent / "in/06_test.in")
fin = (Path(__file__).parent / "in/06.in")
with open(fin, "r") as f:
   fish_list = f.read().split(',')
   fish_list = [int(x) for x in fish_list]

unqiue_starting_vals = list(set(fish_list))

################ Common Function #################

num_fish_by_start_day = {}
pre_calc_days = 256

for start_day in range(0,pre_calc_days):
    days_remaining = start_day - 9
    
    temp_fish = 1

    while days_remaining >= 0:
        temp_fish += num_fish_by_start_day[days_remaining]
        days_remaining -= 7

    num_fish_by_start_day[start_day] = temp_fish

def simulate_x_days(number_days):
    answers_by_start_val = {}

    for val in unqiue_starting_vals:
        answers_by_start_val[val] = 0
        x = number_days - (val + 1)

        while x >= 0:
            answers_by_start_val[val] += num_fish_by_start_day[x]
            x -= 7

    ans = len(fish_list)

    for fish in fish_list:
        ans += answers_by_start_val[fish]

    return ans

################ Part 1 #################

print('ans1:',simulate_x_days(80))

################ Part 2 ################

print('ans2:',simulate_x_days(256))

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))