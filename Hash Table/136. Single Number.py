"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""
""" 异或操作"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=dict()
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        for num in nums:
            if count[num]==1:
                return num

class Solution1(object):
    def singleNumber(self, nums):
        nums_seen = set()
        for i in nums:
            if i in nums_seen:
                nums_seen.remove(i)
            else:
                nums_seen.add(i)
        return nums_seen.pop()