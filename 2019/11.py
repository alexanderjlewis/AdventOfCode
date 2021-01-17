from pathlib import Path
from time import time
from PIL import Image

t0 = time()

################ Data Processing #################

lines = (Path(__file__).parent / "in/11.in").open().read().split(',')
instructions = {}
for i, val in enumerate(lines):
    instructions[i] = int(val)

################ IntCode Computer #################

def position(d,i,ms,rb):
    t = []
    v = []
    for j, m in enumerate(ms):    
        if m == 0:
            t.append(d.get(i+j+1,0))
        elif m == 1:
            t.append(i+j+1)
        else:
            t.append(d.get(i+j+1,0) + rb)      
        v.append(d.get(t[j],0))
    return t,v

class IntcodeComp:
    def __init__(self,instructions):
        self.i = 0
        self.inst = instructions
        self.rb = 0
        
    def compute(self,in_val):
        out = ''
        while self.i < len(self.inst):
            ms = []
            d_in = str(self.inst[self.i]).rjust(5,'0')
            opcode = d_in[3:]
            ms.append(int(d_in[2]))
            ms.append(int(d_in[1]))
            ms.append(int(d_in[0]))
            t, v = position(self.inst,self.i,ms,self.rb)
            if opcode == '01':
                self.inst[t[2]] = v[0] + v[1]
                self.i += 4
            elif opcode == '02':
                self.inst[t[2]] = v[0] * v[1]
                self.i += 4
            elif opcode == '03':
                self.inst[t[0]] = in_val
                self.i += 2
            elif opcode == '04':
                out = v[0]
                self.i += 2
                break
            elif opcode == '05':
                if v[0] != 0:
                    self.i = v[1]
                else:
                    self.i += 3
            elif opcode == '06':
                if v[0] == 0:
                    self.i = v[1]
                else:
                    self.i += 3
            elif opcode == '07':
                self.inst[t[2]] = 1 if v[0] < v[1] else 0
                self.i += 4
            elif opcode == '08':
                self.inst[t[2]] = 1 if v[0] == v[1] else 0
                self.i += 4
            elif opcode == '09':
                self.rb = self.rb + v[0]
                self.i += 2
            else:
                out = None
                break
        return out

################ Part 1 #################

#directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] #0=N,1=E,2=S,3=W
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)] #0=N,1=E,2=S,3=W

class Robot:
    def __init__(self):
        self.d = 0
        self.x = 0
        self.y = 0
        self.comp = IntcodeComp(instructions.copy())
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
            ouput_1 = self.comp.compute(camera)
            ouput_2 = self.comp.compute(None)
            if ouput_1 == None:
                break
            else:
                self.painted[(self.x,self.y)] = ouput_1
            self.turn(ouput_2)
            self.move()
        return self.painted

robot1 = Robot()

print('ans1:',len(robot1.paint(0)))

################ Part 2 #################

robot2 = Robot()
output = robot2.paint(1)


x = max(entry[0] for entry in output) + 1
y = max(entry[1] for entry in output) + 1

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

#computer = IntcodeComp(instructions.copy())

#print('ans2:',computer.compute(2))

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))