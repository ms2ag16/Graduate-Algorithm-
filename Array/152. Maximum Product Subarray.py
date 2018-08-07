"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum,minimum=nums[0],nums[0]
        result=nums[0]
        for num in nums[1:]:
           maximum=max(num,maximum*num,minimum*num)
           minimum=min(num,maximum*num,minimum*num)
           result=max(maximum,result)
        return result

if __name__ == "__main__":
    print Solution().maxProduct([2, 3, -2, 4])
        
