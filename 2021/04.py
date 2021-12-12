
from pathlib import Path
from time import time
from copy import deepcopy
from math import sqrt

t0 = time()

################ Data Processing #################

boards = []
board = []

def format_line(line):
    line = line.strip().replace('  ',' ').split(' ')
    line = [int(x) for x in line]
    return(line)

fin = (Path(__file__).parent / "in/04.in")
with open(fin, "r") as f:
    draw_order = f.readline().strip().split(',')
    draw_order = [int(item) for item in draw_order]
    raw_boards = f.read().split('\n\n')
    raw_boards = [board.strip().replace('\n',' ').replace('  ',' ').split(' ') for board in raw_boards]   
    #boards = [[int(number) for number in board] for board in boards]  

#rint(draw_order)
#print(raw_boards)

board_size = int(sqrt(len(raw_boards[0])))
number_boards = len(raw_boards)

#print(board_size,number_boards)

boards = []

for raw_board in raw_boards:
    board = []
    for i in range(board_size):
        temp_rows = []
        temp_cols = []
        temp_rows = raw_board[i*board_size:(i*board_size)+board_size]
        temp_cols = raw_board[i::board_size]
        string_cols = []
        string_rows = []
        for j in temp_cols:
            string_cols.append(int(j))
        board.append(string_cols)
        for j in temp_rows:
            string_rows.append(int(j))
        board.append(string_rows)
        
    boards.append(board)

#print('boards',boards)

################ Common Function #################



################ Part 1 #################

boards_1 = deepcopy(boards)

moves = 0
finish = False
best_board = 0
best_moves = 10000000

for x, board in enumerate(boards_1):
    moves = 0
    finish = False
    for card in draw_order:
        moves += 1
        for i in range(len(board)):
            board[i] = [num for num in board[i] if num != card]
        for row in board:
            if len(row) == 0:
                finish = True
                break
        if finish:
            if moves < best_moves:
                best_moves = moves
                best_board = x
            break

unmarked_sum = int(sum([sum(x) for x in boards_1[best_board]]) / 2)
last_ball = draw_order[best_moves - 1]

print('ans1:',unmarked_sum * last_ball)

################ Part 2 #################

boards_2 = deepcopy(boards)

moves = 0
finish = False
best_board = 0
best_moves = 0

for x, board in enumerate(boards_2):
    moves = 0
    finish = False
    for card in draw_order:
        moves += 1
        for i in range(len(board)):
            board[i] = [num for num in board[i] if num != card]
        for row in board:
            if len(row) == 0:
                finish = True
                break
        if finish:
            if moves > best_moves:
                best_moves = moves
                best_board = x
            break

unmarked_sum = int(sum([sum(x) for x in boards_2[best_board]]) / 2)
last_ball = draw_order[best_moves - 1]

print('ans2:',unmarked_sum * last_ball)

################ Timing #################

print("Time taken: %dms" % (1000 * (time() - t0)))