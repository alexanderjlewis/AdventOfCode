
from pathlib import Path
from time import time

t0 = time()

################ Data Processing #################

signal_list = []
output_list = []

#fin = (Path(__file__).parent / "in/test/08.in") #(ANS1=26,ANS2=61229)
fin = (Path(__file__).parent / "in/08.in")
with open(fin, "r") as f:
    
    for line in f:
        signal,output = line.strip().split(' | ')
        signal_list.append(signal.split(' '))
        output_list.append(output.split(' '))

################ Common Function #################



################ Part 1 #################

lengths = [2,3,4,7]

count = 0

for outputs in output_list:
    for output in outputs:
        if len(output) in lengths:
            count += 1

print('ans1:',count)

################ Part 2 ################

def string_diff(string_A,string_B):
    # takes two strings as inputs
    # returns all elements that don't appear in both strings

    response = []

    for char in string_A:
        if char in string_B:
            pass
        else:
            response.append(char)
    
    for char in string_B:
        if char in string_A:
            pass
        else:
            response.append(char)

    response = ''.join(set(response))

    return response

def process_input(signal_list,output_list):

    segments = {'A':'','B':'','C':'','D':'','E':'','F':'','G':'',}

    numbers = {0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}

    #### Rule 0 ####
    # find first four numbers based on unique lengths
    remaining_signals = []
    for signal in signal_list:
        if len(signal) == 2:
            numbers[1] = signal
        elif len(signal) == 3:
            numbers[7] = signal
        elif len(signal) == 4:
            numbers[4] = signal
        elif len(signal) == 7:
            numbers[8] = signal
        else:
            remaining_signals.append(signal)

    signals = remaining_signals.copy()
    #### Rule 1 ####
    # Segment 'A' is difference between the 7 and 1 digits

    segments['A'] = numbers[7]

    for char in numbers[1]:
        segments['A'] = segments['A'].replace(char,'')

    #### Rule 2 ####
    # '4' Digit plus Segment 'A' + Segment ? - find the only one with a single extra segment, that's the 9 and Segment 'G'
    test_signal = numbers[4] + segments['A']

    remaining_signals = []
    for signal in signals:
        diff = string_diff(signal,test_signal)
        if len(diff) == 1:
            numbers[9] = signal
            segments['G'] = diff
        else:
            remaining_signals.append(signal)
    
    signals = remaining_signals.copy()

    #### Rule 3 ####
    # Only missing Segment from 9 digit is 'E'
    segments['E'] = string_diff(numbers[9],'abcdefg')

    #### Rule 4 ####
    # '7' Digit + Segment 'G' + Segment ? - find the only one with a single difference, that's the 3 and Segment 'D'
    test_signal = numbers[7] + segments['G']

    remaining_signals = []
    for signal in signals:
        diff = string_diff(signal,test_signal)
        if len(diff) == 1:
            numbers[3] = signal
            segments['D'] = diff
        else:
            remaining_signals.append(signal)

    signals = remaining_signals.copy()

    #### Rule 5 ####
    # Difference between digits 3 and 9 gives Segment 'B'
    segments['B'] = string_diff(numbers[9],numbers[3])

    #### Rule 6 ####
    # '0' digit is 8 digit minus segment 'D'
    test_signal = numbers[8]
    test_signal = test_signal.replace(segments['D'],'')

    remaining_signals = []
    for signal in signals:
        diff = string_diff(signal,test_signal)
        if len(diff) == 0:
            numbers[0] = signal
        else:
            remaining_signals.append(signal)

    signals = remaining_signals.copy()

    #### Rule 7 ####
    # '6' digit is only signal of length 6 left.. nope
    for i in range(len(signals)):
        if len(signals[i]) == 6:
            numbers[6] = signals[i]
            signals.pop(i)
            break

    #### Rule 8 ####
    # difference between digit 6 and 8 is segment C
    segments['C'] = string_diff(numbers[6],numbers[8])

    #### Rule 9 ####
    # digit 1 minuts segment C is segment F
    segments['F'] = numbers[1].replace(segments['C'],'')

    #### Rule 10 ####
    # trivial to fund remianing numbers by assembling known segments
    numbers[2] = segments['A'] + segments['C'] + segments['D'] + segments['E'] + segments['G']
    numbers[5] = segments['A'] + segments['B'] + segments['D'] + segments['F'] + segments['G']

    #### Rules Done ####

    ans = ''

    for entry in output_list:
        for number in numbers:
            diff = string_diff(entry,numbers[number])
            if len(diff) == 0:
                ans = ans + str(number)

    ans = int(ans)

    return ans

ans2 = 0
for i in range(len(signal_list)):
    ans2 += process_input(signal_list[i],output_list[i])

print('ans2:',ans2)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))