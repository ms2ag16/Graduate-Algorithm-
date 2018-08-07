"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.
You may assume no duplicate exists in the array.
Example 1:

Input: [3,4,5,1,2] 
Output: 1
"""

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[left]:
                left=mid+1
            else:
                end=mid
        return nums[left]
        
if __name__=="__main__":
    print Solution().findMin([3,4,5,6,8,9])
