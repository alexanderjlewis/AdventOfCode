
from copy import deepcopy
from pathlib import Path
from time import time
from math import ceil, floor
from itertools import combinations

t0 = time()

################ Data Processing #################

points = []
instructions = []

#fin = (Path(__file__).parent / "in/test/18.in") #(ANS1=4140,ANS2=3993)
fin = (Path(__file__).parent / "in/18.in")
with open(fin, "r") as f:
    data = f.read()
    input_numbers = data.splitlines()

################ Common Function #################

class Pair():
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def explode(self, level=0, occured = False):
        '''explode the left most appropriate pair then return'''
        return_l, return_r = 0,0
        
        if level >= 4 and isinstance(self.left,int) and isinstance(self.right,int):
            if not occured:
                return True, self.left, self.right, True
        else:
            new_level = level + 1
            if isinstance(self.left, Pair):
                exploded, r_l, r_r, occured = self.left.explode(new_level,occured)
                if exploded:
                    self.left = 0
                if isinstance(self.right, Pair):
                    self.right.add_to_left(r_r)
                else:
                    self.right += r_r
                return_l = r_l
            
            if isinstance(self.right, Pair):
                exploded, r_l, r_r, occured = self.right.explode(new_level,occured)
                if exploded:
                    self.right = 0
                if isinstance(self.left, Pair):
                    self.left.add_to_right(r_l)
                else:
                    self.left += r_l
                return_r = r_r

        return False, return_l, return_r, occured

    def add_to_left(self, val):
        '''adds the provided val to the next values to the left, floating through levels as required'''
        if isinstance(self.left, Pair):
            self.left.add_to_left(val)
        else:
            self.left += val

    def add_to_right(self, val):
        '''adds the provided val to the next values to the right, floating through levels as required'''
        if isinstance(self.right, Pair):
            self.right.add_to_right(val)
        else:
            self.right += val

    def split(self, occured=False):
        '''split the left most appropriate value then return'''
        if not occured:
            if isinstance(self.left, Pair):
                occured = self.left.split(occured)
            elif self.left > 9:
                self.left = Pair(floor(self.left/2),ceil(self.left/2))
                occured = True
            
        if not occured:
            if isinstance(self.right, Pair):
                occured = self.right.split(occured)
            elif self.right > 9:
                self.right = Pair(floor(self.right/2),ceil(self.right/2))
                occured = True
        
        return occured

    def get_magnitude(self):
        '''calculates the magnitude of the pair'''
        magnitude = 0

        if isinstance(self.left, Pair):
            magnitude += 3 * self.left.get_magnitude()
        else:
            magnitude += 3 * self.left

        if isinstance(self.right, Pair):
            magnitude += 2 * self.right.get_magnitude()
        else:
            magnitude += 2 * self.right        

        return magnitude

    def __str__(self):
        return '(' + str(self.left) + ',' + str(self.right) + ')'


def parse_string_to_object(str):

    str = str[1:-1]

    if len(str) == 3:
        left, right = str.split(',')
        left = int(left)
        right = int(right)
    else:
        brace_counter = 0
        for i in range(len(str)):
            if str[i] == '[':
                brace_counter += 1
            elif str[i] == ']':
                brace_counter -= 1
            
            if brace_counter == 0:
                left, str = str[:i+1], str[i+1:]
                break

        right = str[1:] #remove the comma character from the start of the string

        if len(left) > 1:
            left = parse_string_to_object(left)
        else:
            left = int(left)
        
        if len(right) > 1:
            right = parse_string_to_object(right)
        else:
            right = int(right)

    return Pair(left, right)

def reduce(number):

    while True: 
        number_in = str(number)

        while True: #repeatedly explode until no more valid pairs to explode
            number_in = str(number)
            number.explode()
            if number_in == str(number):
                break

        number.split() #perform one split actions

        if str(number) == number_in:
            break

    return number

################ Part 1 #################

input_numbers_1 = deepcopy(input_numbers)
input_numbers_1 = [parse_string_to_object(line) for line in input_numbers_1]

output_number = Pair(input_numbers_1.pop(0),input_numbers_1.pop(0))
output_number = reduce(output_number)

while len(input_numbers_1) > 0:
    output_number = Pair(output_number,input_numbers_1.pop(0))
    output_number = reduce(output_number)

print('ans1:',output_number.get_magnitude())

################ Part 2 ################

input_numbers_2 = deepcopy(input_numbers)
number_combinations = list(combinations(input_numbers_2,2))

max_val = 0
for combination in number_combinations:

    input_1 = parse_string_to_object(combination[0])
    input_2 = parse_string_to_object(combination[1])

    order_1 = reduce(Pair(deepcopy(input_1),deepcopy(input_2)))
    order_2 = reduce(Pair(deepcopy(input_2),deepcopy(input_1)))

    max_val = max(order_1.get_magnitude(), order_2.get_magnitude(), max_val)

print('ans2:',max_val)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))