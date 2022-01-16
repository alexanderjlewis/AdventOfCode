
from pathlib import Path
from time import time
from math import prod

t0 = time()

################ Data Processing #################

points = []
instructions = []

#fin = (Path(__file__).parent / "in/test/17.in") #(ANS1=45,ANS2=112)
fin = (Path(__file__).parent / "in/17.in")
with open(fin, "r") as f:
    data = f.read()
    data = data.replace('target area: x=','').replace(' y=','')
    target_x_range,target_y_range = data.split(',')
    target_x_range = target_x_range.split('..')
    target_x_range = [int(x) for x in target_x_range]
    target_y_range = target_y_range.split('..')
    target_y_range = [int(y) for y in target_y_range]

y_absolute_min = min(target_y_range) - 1
x_absolute_max = max(target_x_range) + 1

################ Common Function #################

def launch(vel_x,vel_y):
    x, y = 0,0
    hit_area = False

    max_y = 0

    while True:
        x += vel_x
        y += vel_y

        if vel_x > 0:
            vel_x -= 1
        elif vel_x < 0:
            vel_x += 1    

        vel_y -= 1

        if (x > max(target_x_range)) or (y < min(target_y_range)):
            break
        elif (target_x_range[0] <= x <= target_x_range[1]) and (target_y_range[0] <= y <= target_y_range[1]):
            hit_area = True
            break

        max_y = max(max_y,y)

    return hit_area, max_y

max_y_overall = 0
hits = 0

for x_vel in range(1,x_absolute_max):
    for y_vel in range(y_absolute_min,-y_absolute_min):
        hit_area, max_y = launch(x_vel,y_vel)
        if hit_area:
            max_y_overall = max(max_y_overall,max_y)
            hits += 1

################ Part 1 #################

print('ans1:',max_y_overall)

################ Part 2 ################

print('ans2:',hits)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))