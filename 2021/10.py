
from pathlib import Path
from time import time
from math import prod

t0 = time()

################ Data Processing #################

subsystems = []

#fin = (Path(__file__).parent / "in/test/10.in") #(ANS1=26397,ANS2=288957)
fin = (Path(__file__).parent / "in/10.in")
with open(fin, "r") as f:
    for line in f:
        line = list(line.strip())
        subsystems.append(line)

################ Common Function #################

open_parens = {'(':')','[':']','{':'}','<':'>'}
close_parens = {')':'(',']':'[','}':'{','>':'<'}

illegal_chars = []

incomplete_subsystems = []

for line in subsystems:
    working_array = []
    illegal = False
    
    for char in line:
        if char in open_parens:
            working_array.append(char)
        else:
            if working_array[-1] == close_parens[char]:
                working_array.pop()
            else:
                illegal_chars.append(char)
                illegal = True
                break
    
    if not illegal:
        incomplete_subsystems.append(line)

ans1 = 0

################ Part 1 #################

points1 = {')':3,']':57,'}':1197,'>':25137}

for char in illegal_chars:
    ans1 += points1[char]

print('ans1:',ans1)

################ Part 2 ################

points2 = {')':1,']':2,'}':3,'>':4}

completion_strings = []

for line in incomplete_subsystems:
    working_array = []
    
    for char in line:
        if char in open_parens:
            working_array.append(char)
        else:
            working_array.pop()

    working_array.reverse()

    completion_string = []

    for char in working_array:
        completion_string.append(open_parens[char])

    completion_strings.append(completion_string)

scores = []

for string in completion_strings:
    score = 0
    for char in string:
        score *= 5
        score += points2[char]
    scores.append(score)

scores.sort()

middle_score = scores[int((len(scores) - 1)/2)]

print('ans2:',middle_score)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))