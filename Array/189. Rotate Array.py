"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def reverse(nums,left,right):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                start+=1
                end-=1
        n=len(nums)
        k%=n
        reverse(nums,0,n-k-1)
        reverse(nums,n-k,n-1)
        reverse(nums,0,n-1)
        
