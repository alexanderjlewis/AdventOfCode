from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

#fin = (Path(__file__).parent / "in/test/02.in") #(ANS1=15,ANS2=12)
fin = (Path(__file__).parent / "in/02.in")

rounds = []
with open(fin, "r") as f:
    data = f.read()   
    for record in data.split("\n"):
        rounds.append(record.split(" "))

################ Common Function #################




################ Part 1 #################

values = {"X":1,"Y":2,"Z":3}
win = {"A":"Y","B":"Z","C":"X"}
draw = {"A":"X","B":"Y","C":"Z"}
lose = {"A":"Z","B":"X","C":"Y"}

score = 0

for round in rounds:
    opp = round[0]
    you = round[1]
    
    if win[opp] == you:
        score += 6
    elif draw[opp] == you:
        score += 3
    
    score += values[you]

print('ans1:',score)

################ Part 2 #################

score = 0

for round in rounds:
    opp = round[0]
    result  = round[1]
    
    if result == "X": #need to loose
        you = lose[opp]
    elif result == "Y": #need to dtaw
        you = draw[opp]
        score += 3
    else: #need to win
        you = win[opp]
        score += 6

    score += values[you]

print('ans2:',score)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))