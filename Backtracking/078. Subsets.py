"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        def dfs(current, nums, index, res):
            res.append(current)
            for i in range(index, len(nums)):
                dfs(current+[nums[i]], nums, i+1, res )

        dfs([], nums, 0, res)
        return res



if __name__=="__main__":
    print Solution().subsets([5,6,9])
        
