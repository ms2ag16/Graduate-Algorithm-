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
        res=set()
        sumIndex={}
        
        # get sum of two nums
        for i in range(len(nums)):
            # no duplicate same element (can be same value) in sorted sums
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] in sumIndex:
                    sumIndex[nums[i]+nums[j]].append((i,j))
                else:
                    sumIndex[nums[i]+nums[j]]=((i,j))
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sumNeed=target - nums[i]-nums[j]
                if sumNeed in sumIndex:
                    for index in sumIndex[sumNeed]:
                        if index[0]>j:
                            res.add(tuple(sorted([nums[i],nums[j],nums[index[0]], nums[index[1]]])))
        return (res=map(list,res))
                        
                
        
