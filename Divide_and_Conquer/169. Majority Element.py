"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
""" 

""" DIVIDE AND CONQUER """

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype:
        """
        left=0
        right=len(nums)-1
        if left==right:
            return nums[left]
        mid=(left+right)//2
        left_major=self.majorityElement(nums[:mid+1])
        right_major=self.majorityElement(nums[mid+1:])

        if left_major==right_major:
            return left_major

        left_count=right_count=0
        for i in range(len(nums)):
            if nums[i]==left_major:
                left_count+=1
        for j in range(len(nums)):
            if nums[j]==right_major:
                right_count+=1

        return left_major if left_count>right_count else right_major
        



class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype:
        """
        nums.sort()
        return nums[len(nums)//2]
