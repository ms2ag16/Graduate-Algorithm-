"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        3 pointers left, mid, right
        left and right to mark the subfivision of red and blue
        while mid is the one go over the loop of the list
        """
        left=mid=0
        right=len(nums)-1
        while mid<=right:
            if nums[mid]==0:
                nums[left],nums[mid]=nums[mid],nums[left]
                left+=1
                nums+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[right],nums[mid]=nums[mid],nums[right]
                right-=1
                
if __name__ == "__main__":
    l = [1, 2, 1, 2, 0, 2, 1, 0, 2, 0, 0, 2]
    Solution().sortColors(l)
    assert l == [0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
