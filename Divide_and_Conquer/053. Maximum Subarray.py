"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
""" 

""" Dynamic Programming """
""" Dynamic Programming looping over the nums and use space of O(n)"""
class Solution(object):
    def maxSubArray(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=nums
        for i in range(1,len(nums)):
            sum[i]=max(nums[i],sum[i-1]+nums[i])
            
        return max(sum)
            

""" DIVIDE AND CONQUER """
""" Merge Sort similar in recursion part O(nlogn), CrossingSumPart is Linear O(n)"""
class Solution(object):
    def maxCrossingSum(self, nums, low, mid, high):
        # include elements on the left of mid
        sm=0
        left_sum=nums[mid]
        for i in range(mid, low-1,-1):
            sm+=nums[i]
            if (sm>left_sum):
                left_sum=sm

        #include elements on the right of mid
        sm=0
        right_sum=nums[mid+1]
        for i in range(mid+1,high+1):
            sm+=nums[i]
            if (sm>right_sum):
                right_sum=sm

        return left_sum+right_sum



    def maxSubArray(self,nums):
        low=0
        high=len(nums)-1

        if low==high:
            return nums[low]

        #find mid point
        mid=(low+high)//2

        return max(self.maxSubArray(nums[low:mid+1]),
                   self.maxSubArray(nums[mid+1:high+1]),
                   self.maxCrossingSum(nums,low, mid, high))
