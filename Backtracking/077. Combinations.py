"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

# backtracking using recurssion

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res=[]
        def dfs(current, n, k, index, res):
            if k==0:
                res.append(current)
                return
            for i in range(index+1, n+1):
                dfs(current+[i], n, k-1, i, res)
        dfs([], n, k, 0, res)
        return res
