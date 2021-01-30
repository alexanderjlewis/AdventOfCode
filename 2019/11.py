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

class Robot:
    def __init__(self):
        self.d = 0
        self.pos = (0,0)
        self.comp = IntcodeComp(instructions.copy())
        self.painted = {}
        self.directions = [(0, -1), (1, 0), (0, 1), (-1, 0)] #0=N,1=E,2=S,3=W   

    def turn(self,direction):
        self.d = ((self.d + 1) % 4) if direction == 1 else ((self.d - 1 + 4) % 4)

    def move(self):
        self.pos = tuple(sum(coord) for coord in zip(self.pos, self.directions[self.d]))

    
    def paint(self, starting_colour):
        self.painted = {self.pos:starting_colour}
        while True:   
            camera = self.painted[self.pos] if self.pos in self.painted else 0
            ouput_1 = self.comp.compute([camera])
            if ouput_1 == None:
                break
            else:
                self.painted[self.pos] = ouput_1
            self.turn(self.comp.compute())
            self.move()
        return self.painted

robot = Robot()

print('ans1:',len(robot.paint(0)))

################ Part 2 #################

robot = Robot()
output = robot.paint(1)

w, h = max(entry[0] for entry in output) + 1, max(entry[1] for entry in output) + 1

im = Image.new('RGB', (w+2,h+2),"black")

out = []
for i in range(h):
    for j in range(w):
        val = output.get((j,i),0)
        if val == 1:
            im.putpixel((j+1, i+1), (255, 255, 255, 255))
            out.append('#')
        else:
            im.putpixel((j+1, i+1), (0, 0, 0, 255))
            out.append(' ')

print('ans2:')
for i in range(0, len(out), w):
    print(*out[i:i + w], sep='')

im.show()

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))