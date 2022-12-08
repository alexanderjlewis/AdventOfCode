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

def calc_dir_size(dirs):
    
    value = 0

    while True:
        a,*b = commands.pop(0)

        if a == "$": #it's a commmand
            if b[0] == "cd" and b[1] == "..":
                
                dirs.append(value)
                break

            elif b[0] == "cd": #this mean we are changing to a new directory
                inner_value,dirs = calc_dir_size(dirs)
                value += inner_value

            else:   #means command is LS and we just move on
                pass
    
        else: #it's a file or dir

            if a != "dir": #it's a file, so we add it's size on
                value += int(a)

        if len(commands) == 0:
            dirs.append(value)
            break

    return value,dirs


################ Part 1 #################

commands.pop(0) #remove the "$ cd /" at start of file
_,dirs = calc_dir_size([])

print('ans1:',sum(dir for dir in dirs if dir <= 100000))

################ Part 2 #################

free_space = 70000000 - max(dirs)
extra_space_required = 30000000 - free_space

delta = free_space
dir_size = 0

for dir in dirs:
    if dir >= extra_space_required:
        if (dir-extra_space_required) < delta:
            delta = (dir-extra_space_required)
            dir_size = dir

print('ans2:',dir_size)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))