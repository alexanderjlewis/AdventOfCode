from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

fin = (Path(__file__).parent / "in/06.in").open().read()
groups = fin.split('\n\n')

################ Common Function #################

group_any_yes = []
group_all_yes = []

for group in groups:
    s = set(group)
    s.discard('\n')
    group_any_yes.append(s)

    counter_all = 0
    group_number_people = group.count('\n') + 1
    for char in s:
        if group.count(char) == group_number_people:
            counter_all += 1
    group_all_yes.append(counter_all)

################ Part 1 #################

print('ans1:',sum(len(x) for x in group_any_yes))

################ Part 2 #################

print('ans2:',sum(group_all_yes))

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))