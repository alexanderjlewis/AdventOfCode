from pathlib import Path
from time import time

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
            m = []
            d_in = str(self.inst[self.i]).rjust(5,'0')
            opcode = d_in[3:]
            print(opcode)
            m.append(int(d_in[2]))
            m.append(int(d_in[1]))
            m.append(int(d_in[0]))
            t, v = position(self.inst,self.i,m,self.rb)
            print(t,v)
            if opcode == '01':
                self.inst[t[2]] = v[0] + v[1]
                self.i += 4
            elif opcode == '02':
                self.inst[t[2]] = v[0] * v[1]
                self.i += 4
            elif opcode == '03':
                self.inst[t[2]] = in_val
                self.i += 2
            elif opcode == '04':
                out = v[0]
                self.i += 2
                #k = list(self.inst.items())
                #print(k[:150])
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

    def turn(self,direction):
        #print(turn,self.d)
        #print('direction',direction)
        if direction == 1:
            #print('1b',self.d)
            self.d = (self.d + 1) % 4
            #print('1a',self.d)
        elif direction == 0:
            #print('0b',self.d)
            self.d = (self.d - 1 + 4) % 4
            #print('0a',self.d)

    def move(self):
        self.x = self.x + directions[self.d][0]
        self.y = self.y + directions[self.d][1]
        return ((self.x,self.y))

painted = {(0,0):0}
l = (0,0)

computer = IntcodeComp(instructions.copy())
robot = Robot()

#while True:
for i in range(3):
    
    a = painted[l] if l in painted else 0
    print('comp in',a)
    #print('starting pos',robot.x,robot.y,robot.d)
    #print(l,robot.d,painted)

    o1 = computer.compute(a)
    o2 = computer.compute(a)
    #print('output of comp',o1,o2)
    if o1 == None:
        break
    else:
        #print('l,c',l,c)
        painted[l] = o1

    robot.turn(o2)
    l = robot.move()
    print('ending pos',robot.x,robot.y,robot.d,painted)
    print('#### NEXT #####')
    

print(len(painted))
#print(painted)


#print('ans1:',computer.compute(1))

################ Part 2 #################

#computer = IntcodeComp(instructions.copy())

#print('ans2:',computer.compute(2))

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))