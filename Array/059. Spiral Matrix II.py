"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        left=top=0
        right=n-1
        bottom = n-1
        num=1
        result=[[0 for _ in range(n)] for _ in range (n)]

        while left<right and top<bottom:
            for i in range(left, right):
                result[top][i]=num
                num+=1
            for i in range(top,bottom):
                result[i][right]=num
                num+=1
            for i in range(right,left,-1):
                result[bottom][i]=num
                num+=1
            for i in range(bottom, top,-1):
                result[i][left]=num
                num+=1
            left+=1
            right-=1
            top+=1
            bottom-=1
        if n%2==1:
            result[top][left]=num
            print num
        return result



if __name__=='__main__':
    print Solution().generateMatrix(5)
