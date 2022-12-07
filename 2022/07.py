from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

fin = (Path(__file__).parent / "in/test/07.in") #(ANS1=95437,ANS2=)
#fin = (Path(__file__).parent / "in/07.in")

commands = []
with open(fin, "r") as f:
    datastream = f.read()
    commands = [a.split(" ") for a in datastream.split("\n")]

print(commands)

commands.pop(0) #remove the "$ cd /" at start of file

dirs_under_10k = {}

def calc_dir_size(dir):
    value = 0

    while True:
        if commands[0][0] == "$": #it's a commmand
            if commands[0][4] == "$ cd ..":
                commands.pop(0)

                if value <= 10000:
                    dirs_under_10k[dir] = value

                break
            elif commands[0][4] == "$ ls":
                commands.pop(0)
            else:
                _,_,next_dir = commands[0].split(" ")
                value
        else: #it's a file or dir


    
    commands.pop(0)
    
    return



while len(commands) > 0:
    o = []

    current_command = commands[0]

    if current_command[0] == "$":
        if current_command[1] == "ls":
            commands.pop(0)
            while True:

        else: #must be a cd
            if current_command[2] == "..": #move up a dir

            else: #must be change to a lower dir

    else: #line is an output
        if current_command[0] == "dir":

        else: #it's a file
        


################ Common Function #################

def process_dir(dir_contents):
    pass

################ Part 1 #################

value = 0

print('ans1:',value)

################ Part 2 #################

print('ans2:',)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))