"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.


A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true

"""036. Valid Sudoku



class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            if not self.isValid(board[i]):
                return False
            col=[c[i] for c in board]
            if not self.isValid(col):
                return False
        
        for i in [0,3,6]:
            for j in [0,3,6]:
                block=[board[s][t] for s in [i,i+1,i+2] for t in [j,j+1,j+2]]
                if not self.isValid(block):
                    return False
        
        return True
    
    def isValid(self,row):
        map={}
        for c in row:
            if c !='.':
                if c in map:
                    return False
                else:
                    map[c]=True
        return True
        
