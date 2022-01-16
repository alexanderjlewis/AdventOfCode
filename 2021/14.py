
from pathlib import Path
from time import time
from typing import runtime_checkable

t0 = time()

################ Data Processing #################

points = []
instructions = []

#fin = (Path(__file__).parent / "in/test/14.in") #(ANS1=1588,ANS2=2188189693529)
fin = (Path(__file__).parent / "in/14.in")
with open(fin, "r") as f:
    data = f.read()
    template,raw_rules = data.split('\n\n')
    rules = {}
    blank_pairs = {}
    for rule in raw_rules.splitlines():
        i, o = rule.split(' -> ')
        rules[i] = o
        blank_pairs[i] = 0

################ Common Function #################

def run_steps(template,steps):

    blank_pairs = {k:0 for k,v in rules.items()}

    current_pairs = blank_pairs.copy() 
    for i in range(len(template) - 1):
        pair = template[i] + template[i+1]
        current_pairs[pair] = current_pairs.get(pair, 0) + 1

    for _ in range(steps):
        next_pairs = blank_pairs.copy()
        for k,v in current_pairs.items():
            new_char = rules[k]
            next_pairs[k[0] + new_char] += v
            next_pairs[new_char + k[1]] += v
        current_pairs = next_pairs.copy()

    unique_chars = list(set(rules.values()))
    char_counts = {k:0 for k in unique_chars}

    for k,v in current_pairs.items():
        char_counts[k[0]] += v
        char_counts[k[1]] += v

    char_counts[template[0]] += 1
    char_counts[template[-1]] += 1

    char_counts = [int(v/2) for v in char_counts.values()]

    return max(char_counts) - min(char_counts)

################ Part 1 #################

print('ans1:',run_steps(template,10))

################ Part 2 ################

print('ans2:',run_steps(template,40))

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))