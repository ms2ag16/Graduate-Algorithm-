"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.
Example:

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:
X X X X
X X X X
X X X X
X O X X

Explanation:
Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'.
Any 'O' that is not on the border and it is not connected 
to an 'O' on the border will be flipped to 'X'.
Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        if not board or not board[0]:
            return 
        m=len(board)
        n=len(board[0])
        queue=[]
        for i in range(m):
            for j in range(n):
                if ( (i in (0,m-1)) or (j in (0,n-1))) and board[i][j]=='O':
                    board[i][j]='M'
                    queue.append((i,j))
        
        while queue:
            r,c=queue.pop(0)
            if (r-1)>=0 and board[r-1][c]=='O':
                queue.append((r-1, c))
                board[r-1][c]='M'
            if (r+1)<m and board[r+1][c]=='O':
                queue.append((r+1, c))
                board[r+1][c]='M'
            if (c-1)>=0 and board[r][c-1]=='O':
                queue.append((r, c-1))
                board[r][c-1]='M'
            if (c+1)<n and board[r][c+1]=='O':
                queue.append((r, c+1))
                board[r][c+1]='M'
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=='M':
                    board[i][j]='O'
                else:
                    board[i][j]='X'
