from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

lines = (Path(__file__).parent / "in/09.in").open().read().split(',')
instructions = {}
for i, val in enumerate(lines):
    instructions[i] = int(val)

################ Part 1 #################

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
            m.append(int(d_in[2]))
            m.append(int(d_in[1]))
            m.append(int(d_in[0]))
            t, v = position(self.inst,self.i,m,self.rb)
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

computer = IntcodeComp(instructions.copy())

print('ans1:',computer.compute(1))

################ Part 2 #################

computer = IntcodeComp(instructions.copy())

print('ans2:',computer.compute(2))

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))