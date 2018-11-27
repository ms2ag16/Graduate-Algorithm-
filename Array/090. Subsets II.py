"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res=[]
        return self.dfs(0,[],nums,res)

    def dfs(self, start, path, nums,res):
        res.append(path)
        for i in range(start,len(nums)):
            if i!=start and nums[i]==nums[i-1]:
                continue
            self.dfs(i+1, path+[nums[i]], nums, res)
        return res




if __name__=='__main__':
    print  (Solution().subsetsWithDup([1,2,2]))
