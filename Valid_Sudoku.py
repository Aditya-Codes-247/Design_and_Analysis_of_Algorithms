import numpy as np
import re
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        c = 0
        board = np.array(board)
        for col in board.T:
            n_arr = np.array(col)
            n_arr = [int(num) for string in n_arr for num in re.findall(r'\d+', string)]
            if (len(n_arr) != len(set(n_arr))):
                c= c+1
            else:
                continue
        for row in board:
            n_arr = np.array(row)
            n_arr = [int(num) for string in n_arr for num in re.findall(r'\d+', string)]
            if(len(n_arr) != len(set(n_arr))):
                c = c+1
            else:
                continue
        for i in range(0,9,3):
            for j in range(0,9,3):
                square = [board[row][col] for row in range(i, i+3) for col in range(j, j+3)]
                flat = [
                    square[row][col] 
                    for row in range(len(square)) 
                    for col in range(len(square[0])) 
                    if square[row][col].isdigit()
                ]
                if len(flat) != len(set(flat)):
                    c = c+1
        if(c!=0):
            return False
        else:
            return True

