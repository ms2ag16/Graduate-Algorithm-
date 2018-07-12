"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        
        left=0
        right=len(nums)-1
        
        while left<=right:
            mid=(left+right)/2
            
            if nums[mid]==target:
                return True
            
            if nums[left]==nums[right]==nums[mid]:
                left+=1
                right-=1
            elif nums[mid]>=nums[left]: # left part is organized
                if nums[left]<=target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if nums[mid]<target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return False
                
        

