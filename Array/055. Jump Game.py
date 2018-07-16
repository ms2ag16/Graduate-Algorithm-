"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Example 1:
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        length=len(nums)
        index=0
        longest=nums[0]
        while index <=longest:
            if longest>=length-1:
                return True
            longest=max(longest,index+nums[index])
            index+=1
        return  False

if __name__ == "__main__":
    print Solution().canJump([2, 3, 1, 1, 4])
