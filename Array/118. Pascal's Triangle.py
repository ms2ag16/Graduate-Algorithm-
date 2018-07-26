"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal_rows=[]
        for i in range(numRows):
            if i==0:
                pascal_rows.append([1])
            elif i==1:
                pascal_rows.append([1,1])
            else:
                cur_row=[1]
                for j in range(len(pascal_rows[i-1])-1):
                    cur_row_num=pascal_rows[i-1][j]+pascal_rows[i-1][j+1]
                    cur_row.append(cur_row_num)
                cur_row.append(1)
                pascal_rows.append(cur_row)
        return pascal_rows
    
 if __name__ == "__main__":
    print Solution().generate(4)              
          
