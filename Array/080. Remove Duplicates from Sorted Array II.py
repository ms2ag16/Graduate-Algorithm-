"""
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It doesn't matter what you leave beyond the returned length.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start=0
        for i in range(len(nums)):
            if nums[start-2]!=nums[i] or i<2:
                nums[start]=nums[i]
                start+=1
        return start
    
if __name__ == "__main__":
    print Solution().removeDuplicates([0,0,1,1,1,1,2,3,3])

            
        
        
