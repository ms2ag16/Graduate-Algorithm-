"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.
Input: 3
Output: [1,3,3,1]
"""
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res=[1]+[0]*rowIndex
        for i in range(rowIndex):
            result[0]=1
            for j in range(i+1, 0, -1):
                res[j]=res[j]+rest[j-1]
        return res
if __name__ == "__main__":
    print Solution().getRow(3)
