"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were 
inserted in order.

You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r=0, len(nums)-1
        while l<=r:
           mid=(l+r)/2
           if nums[mid]<target:
             l=mid+1
           else:
             if nums[mid]==target and nums[mid-1]!=target:
               return mid
             else:
               r=mid-1
        return l


if __name__ == "__main__":
    print Solution().searchInsert([1, 3, 5, 6], 5)
    assert Solution().searchInsert([1, 3, 5, 6], 2) == 1    
