"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
          return 0
        start=0
        for i in range(1,len(nums)):
            if nums[start]!=nums[i]:
                start+=1
                nums[start]=nums[i]
                print ('start={0}, nums[start]={0}'.format(start, nums[start]))
        return start+1



if __name__ == "__main__":
    print Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])
      
      
