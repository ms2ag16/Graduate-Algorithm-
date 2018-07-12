"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
      
        result = []
        length = len(nums)

        start = 0
        end = length

        while start < end:
            mid = (start + end) / 2
            if nums[mid] == target and (mid == 0 or nums[mid - 1] != target):
                result.append(mid)
                break
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        if not result:
            return [-1,-1]

        end = length
        while start < end:
            mid = (start + end) / 2
            if nums[mid] == target and (mid==length-1 or nums[mid+1] != target):
                result.append(mid)
                break
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid

        return result
