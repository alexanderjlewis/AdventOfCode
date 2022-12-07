from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

#fin = (Path(__file__).parent / "in/test/07.in") #(ANS1=95437,ANS2=24933642)
fin = (Path(__file__).parent / "in/07.in")

commands = []
with open(fin, "r") as f:
    datastream = f.read()
    commands = [a.split(" ") for a in datastream.split("\n")]

################ Common Function #################

def calc_dir_size():
    
    value = 0

    while True:
        current_command = commands.pop(0)

        if current_command[0] == "$": #it's a commmand
            if current_command[1] == "cd" and current_command[2] == "..":
                
                dirs.append(value)
                break

            elif current_command[1] == "cd": #this mean we are changing to a new directory
                value += calc_dir_size()
            
            #note we can ignore an LS command - doesn't do anything on its own
    
        else: #it's a file or dir

            if current_command[0] != "dir": #it's a file, so we add it's size on
                value += int(current_command[0])

        if len(commands) == 0:
            dirs.append(value)
            break

    return value


################ Part 1 #################

commands.pop(0) #remove the "$ cd /" at start of file
dirs = []
_ = calc_dir_size()

sum_over100k = 0
for dir in dirs:
    if dir <= 100000:
        sum_over100k += dir

print('ans1:',sum_over100k)

################ Part 2 #################

free_space = 70000000 - max(dirs)
extra_space_required = 30000000 - free_space

delta = 70000000
size = 0

for dir in dirs:
    if dir >= extra_space_required:
        if (dir-extra_space_required) < delta:
            delta = (dir-extra_space_required)
            size = dir

print('ans2:',size)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))