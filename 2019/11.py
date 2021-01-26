from pathlib import Path
from time import time
from lib.intcode import IntcodeComp
from PIL import Image

t0 = time()

################ Data Processing #################

lines = (Path(__file__).parent / "in/11.in").open().read().split(',')
instructions = {}
for i, val in enumerate(lines):
    instructions[i] = int(val)

################ Part 1 #################

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)] #0=N,1=E,2=S,3=W

class Robot:
    def __init__(self):
        self.d = 0
        self.x = 0
        self.y = 0
        self.comp = IntcodeComp(instructions)
        self.painted = {}

    def turn(self,direction):
        self.d = ((self.d + 1) % 4) if direction == 1 else ((self.d - 1 + 4) % 4)

    def move(self):
        self.x = self.x + directions[self.d][0]
        self.y = self.y + directions[self.d][1]
    
    def paint(self, starting_colour):
        self.painted = {(self.x,self.y):starting_colour}
        while True:   
            camera = self.painted[(self.x,self.y)] if (self.x,self.y) in self.painted else 0
            ouput_1 = self.comp.compute([camera])
            ouput_2 = self.comp.compute([])
            if ouput_1 == None:
                break
            else:
                self.painted[(self.x,self.y)] = ouput_1
            self.turn(ouput_2)
            self.move()
        return self.painted

robot = Robot()

print('ans1:',len(robot.paint(0)))

################ Part 2 #################

robot = Robot()
output = robot.paint(1)

x, y = max(entry[0] for entry in output) + 1, max(entry[1] for entry in output) + 1

im = Image.new('RGB', (x+2,y+2),"black")

out = []
for i in range(y):
    for j in range(x):
        val = output.get((j,i),0)
        if val == 1:
            im.putpixel((j+1, i+1), (255, 255, 255, 255))
            out.append('#')
        else:
            im.putpixel((j+1, i+1), (0, 0, 0, 255))
            out.append(' ')

print('ans2:')
for i in range(0, len(out), x):
    print(*out[i:i + x], sep='')

im.show()

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))