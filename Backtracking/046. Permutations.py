"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        
        def dfs(nums, current, res):
          if not nums：
            res.append(current)
          else:
            for  i in range(len(nums)):
              dfs(nums[:i]+nums[i+1:], current+[nums[i]], res)
       
        dfs(nums, [], res)
        return res
        
        
