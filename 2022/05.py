from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

fin = (Path(__file__).parent / "in/test/05.in") #(ANS1="CMZ",ANS2=)
#fin = (Path(__file__).parent / "in/05.in")

procedures = []
stacks = []
with open(fin, "r") as f:
    data = f.read()
    drawing, procedure_data = data.split("\n\n")   

    procedure_data = procedure_data.replace('move ',"").replace(' to ',",").replace(' from ',",")
    procedures = [list(map(int,a.split(','))) for a in procedure_data.split("\n")]

    drawing = drawing.replace('   ','#').replace('[',"").replace(']',",").replace(' ',",")

  
################ Common Function #################



################ Part 1 #################

print(procedures)
print(drawing)

print('ans1:',)

################ Part 2 #################



print('ans2:',)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))