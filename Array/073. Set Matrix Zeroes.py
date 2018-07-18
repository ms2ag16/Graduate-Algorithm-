"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:
Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        first_row=first_col=False
        nrow=len(matrix)
        ncol=len(matrix[0])
        
        for i in range(nrow):
            if matrix[i][0]==0:
                first_col=True
        for i in range(ncol):
            if matrix[0][i]==0:
                first_row=True
        
        for row in range(1,nrow):
            for col in range(1,ncol):
                if matrix[row][col]==0:
                    matrix[row][0]=matrix[0][col]=0 """ mark the correspoding first_row/col to 0"""
        """ loop the matrix, to change the numbers"""
        for row in range(1,nrow):
            for col in range(1,ncol):  
                if matrix[0][col]==0 or matrix[row][0]==0:
                    matrix[row][col]=0
        
        """ deal with the first_row and first_col"""
        if first_row:
            for col in range(ncol):
                matrix[0][col]=0
        if first_col:
            for row in range(nrow):
                matrix[row][0]=0

                    
                
                
