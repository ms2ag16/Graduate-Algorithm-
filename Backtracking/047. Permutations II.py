"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        self.dfs(nums, res,[])
        return res

    def dfs(self, nums, res, current):
        if not nums:
            res.append(current)
        else:
            for i in range(len(nums)):
                if nums[i]==nums[i-1] and i-1>=0:
                    continue
                self.dfs(nums[i+1:]+nums[:i], res, current + [nums[i]])
