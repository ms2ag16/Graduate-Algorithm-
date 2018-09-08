"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
The solution set must not contain duplicate quadruplets.

Example:
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        if len(nums)<4:
          return []
        nums.sort()
        res=set()
        sumsIndex={}
        
        """ Get all two elements sum and indexes map."""
        for i in range(len(nums)):
          for j in range(i+1, len(nums)):
            if nums[i]+nums[j] in sumsIndex:
              sumsIndex[nums[i]+nums[j]].append((i,j))
            else:
              sumsIndex[nums[i]+nums[j]]=[(i,j)]
        
        for i in range(len(nums)):
          for j in range(i+1, len(nums)):
            sumNeed=target-nums[i]-nums[j]
            if sumNeed in sumsIndex:
              for index in sumsIndex[sumNeed]:
                if index[0]>j:
                  res.add(tuple(sorted([nums[i],nums[j],nums[index[0]], nums[index[1]]])))
        
        return (res=map(list, res))
              

if __name__ == "__main__":
    assert Solution().fourSum([1, 0, -1, 0, -2, 2], 0) == [[-1, 0, 0, 1], [-2, 0, 0, 2], [-2, -1, 1, 2]]

