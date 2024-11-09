"""Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
    """

from collections import defaultdict
import numpy as np

row_chek = defaultdict()
column_check = defaultdict()
mat_chek = defaultdict()

def check(row):
    values = []
    values2 = []
    for i in row:
        if i == '.':
            pass
        else:
            values.append(i)

    for j in values:
        j = int(j)
        if j > 0 and j < 10:
            values2.append(j)
        else:
            pass
    
    val_set = set(values2)

    if len(values) == len(values2) == len(val_set):
        return True
    else:
        return False


board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

board_array = np.array(board)
for i, row in enumerate(board_array):
    row_chek[i] = check(row)

t_board_array = board_array.T
for i, row in enumerate(t_board_array):
    column_check[i] = check(row)

subarrays = []
for i in range(0, 9, 3):  # iterate over rows, skipping 3 at a time
    for j in range(0, 9, 3):  # iterate over columns, skipping 3 at a time
        subarray = np.array([row[j:j+3] for row in board_array[i:i+3]]).flatten()  # extract the 3x3 subarray and make a list
        subarrays.append(subarray)

for i, row in enumerate(subarrays):
    mat_chek[i] = check(row)

# print(row_chek.values(), column_check.values(), mat_chek.values())

if all(row_chek.values()) and all(column_check.values()) and all(mat_chek.values()):
    print(True)
else:
    print(False)
