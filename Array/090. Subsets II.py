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
        result=[[]]
        temp=0
        nums.sort()
        for i in range(len(nums)):
            if i>=1 and nums[i]==nums[i-1]:
                start=temp
            else:
                start=0
            temp=len(result)
            for j in range(start,temp):
                result.append(result[j]+[nums[i]])
        return result

if __name__=='__main__':
    print  Solution().subsetsWithDup([1,2,2])
