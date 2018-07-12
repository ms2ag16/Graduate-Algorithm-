"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left =0
        right=len(nums)-1
        
        while left<=right:
            mid=(left+right)/2
            
            if nums[mid]==target:
                return mid
            
            if nums[mid]>nums[left]: # left part is organized
                if nums[left]<=target<numd[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else: # right part is organized
                if nums[mid]<target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
         return -1
    
