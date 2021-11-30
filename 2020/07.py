from pathlib import Path
from time import time
import math

t0 = time()

################ Data Processing #################

fin = (Path(__file__).parent / "in/07.in").open().readlines()

################ Common Function #################



################ Part 1 #################

counter1 = 0

rules = {}
for line in fin:
    outer_bag,inner_bags = line.split(' bags contain ')
    inner_bags = inner_bags.replace('.','').replace('\n','').split(', ')
    
    unique_items = []
    for bag in inner_bags:
        if not bag == 'no other bags':
            bag_qty = bag[0] #get the number from the start of the string
            bag_name = [bag[2:].replace(' bags','').replace(' bag','')] #get the type of bag from the end of the string and strip the uneccessary bit
            unique_items.extend(bag_name)

    rules[outer_bag] = unique_items

goal = 'shiny gold'

for rule in rules:
    rule_list_copy = rules[rule].copy()
    while len(rule_list_copy) > 0:
        if goal in rule_list_copy:
            counter1 += 1
            break
        else:
            next_bag_to_check = rule_list_copy.pop()
            next_bag_content = rules[next_bag_to_check]
            rule_list_copy.extend(next_bag_content)

print('ans1:',counter1)

################ Part 2 #################

goal = 'shiny gold'
counter2 = 0

rules = {}
for line in fin:
    outer_bag,inner_bags = line.split(' bags contain ')
    inner_bags = inner_bags.replace('.','').replace('\n','').split(', ')
    
    items = []
    for bag in inner_bags:
        if not bag == 'no other bags':
            bag_qty = bag[0] #get the number from the start of the string
            bag_name = [bag[2:].replace(' bags','').replace(' bag','')] * int(bag_qty) #get the type of bag from the end of the string and strip the uneccessary bits, then add it to array the 'qty' number of times
            items.extend(bag_name)

    rules[outer_bag] = items

rule_list_copy = rules['shiny gold'].copy()
while len(rule_list_copy) > 0:
    next = rules[rule_list_copy.pop()]
    if next == []:
        counter2 += 1
    else:
        counter2 += 1
        rule_list_copy.extend(next)

print('ans2:',counter2)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))