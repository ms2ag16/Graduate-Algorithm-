"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2

Divide and Conquer
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)//2]
        
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        return self.majority(nums,0,len(nums)-1)
    
    def majority(self, nums, left, right):
        if left==right:
            return nums[left]
        mid=(left+right)/2
        m_left=self.majority(nums, left, mid)
        m_right=self.majority(nums, mid+1,right)
        
        if m_left==m_right:
            return m_left
        
        left_count=right_count=0
        for i in range(left, right+1):
            if nums[i]==m_left:
                left_count+=1
            elif nums[i]==m_right:
                right_count+=1
        return m_left if left_count>right_count else m_right
    
