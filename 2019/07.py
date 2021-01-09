from pathlib import Path
from time import time
import itertools

t0 = time()

################ Data Processing #################

lines = (Path(__file__).parent / "in/07.in").open().read().split(',')
instructions = list(map(int,lines))

################ Part 1 #################

def mode(d,i,p1,p2):
    try:
        if p1 == 0:
            t1 = d[d[i+1]]
        else:
            t1 = d[i+1]
        if p2 == 0:
            t2 = d[d[i+2]]
        else:
            t2 = d[i+2]
    except:
        t1 = None
        t2 = None
    return t1,t2

class IntcodeComp:
    def __init__(self,instructions,setting):
        self.i = 0
        self.inst = instructions
        self.setting = setting
        
    def compute(self,in_val):
        out = ''
        while self.i < len(self.inst):
            d_in = str(self.inst[self.i]).rjust(5,'0')
            opcode = d_in[3:]
            p1 = int(d_in[2])
            p2 = int(d_in[1])
            t1, t2 = mode(self.inst,self.i,p1,p2)
            if opcode == '01':
                self.inst[self.inst[self.i+3]] = t1 + t2
                self.i += 4
            elif opcode == '02':
                self.inst[self.inst[self.i+3]] = t1 * t2
                self.i += 4
            elif opcode == '03':
                if self.setting == None:
                    self.inst[self.inst[self.i+1]] = in_val
                else:
                    self.inst[self.inst[self.i+1]] = self.setting
                    self.setting = None
                self.i += 2
            elif opcode == '04':
                if p1 == 0:
                    out = self.inst[self.inst[self.i+1]]
                else:
                    out = self.inst[self.i+1]
                self.i += 2
                break
            elif opcode == '05':
                if t1 != 0:
                    self.i = t2
                else:
                    self.i += 3
            elif opcode == '06':
                if t1 == 0:
                    self.i = t2
                else:
                    self.i += 3
            elif opcode == '07':
                self.inst[self.inst[self.i+3]] = 1 if t1 < t2 else 0
                self.i += 4
            elif opcode == '08':
                self.inst[self.inst[self.i+3]] = 1 if t1 == t2 else 0
                self.i += 4
            else:
                out = None
                break
        return out

def thrust(seq):
    amps = []
    for item in seq:
        amps.append(IntcodeComp(instructions[:],item))

    val = 0
    for amp in amps:
        val = amp.compute(val)
    return val

print('ans1:',max(thrust(seq) for seq in list(itertools.permutations([0,1,2,3,4]))))

################ Part 2 #################

def thrust2(seq):
    amps = []
    for item in seq:
        amps.append(IntcodeComp(instructions[:],item))

    val = 0
    while True:#
        temp = val
        for amp in amps:
            val = amp.compute(val)
        if val == None:
            val = temp
            break
    return val

print('ans2:',max(thrust2(seq) for seq in list(itertools.permutations([5,6,7,8,9]))))

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))
