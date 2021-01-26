
class IntcodeComp:
    def __init__(self,instructions,in_val=[]):
        self.i = 0
        self.inst = instructions.copy()
        self.rb = 0
        self.out = 0
        self.input = in_val.copy()
        self.waiting_for_input = False
    
    def position(self,ms):
        t = []
        v = []
        for j, m in enumerate(ms):    
            if m == 0:
                t.append(self.inst.get(self.i+j+1,0))
            elif m == 1:
                t.append(self.i+j+1)
            else:
                t.append(self.inst.get(self.i+j+1,0) + self.rb)      
            v.append(self.inst.get(t[j],0))
        return t,v

    def compute(self,in_val=[]):
        self.input.extend(in_val)
        out = ''
        while self.i < len(self.inst):
            ms = []
            d_in = str(self.inst[self.i]).rjust(5,'0')
            opcode = d_in[3:]
            ms.extend([int(d_in[2]),int(d_in[1]),int(d_in[0])])
            t, v = self.position(ms)
            if opcode == '01':
                self.inst[t[2]] = v[0] + v[1]
                self.i += 4
            elif opcode == '02':
                self.inst[t[2]] = v[0] * v[1]
                self.i += 4
            elif opcode == '03':
                if len(self.input) > 0:
                    self.waiting_for_input = False
                    self.inst[t[0]] = self.input[0]
                    self.input.pop(0)
                    self.i += 2
                else:
                    self.waiting_for_input = True
                    self.out = None
                    break
            elif opcode == '04':
                self.out = v[0]
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
                self.out = None
                break
        return self.out
