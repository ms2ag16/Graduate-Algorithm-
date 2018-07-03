""" 
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closet_sum=pow(2,32)-1
        for i in range(len(nums)-2):
            """ remove duplicate situation """
            if i==0 or nums[i]>nums[i-1]:
                left=i+1
                right =len(nums)-1
                while left<right:
                    diff=nums[left]+nums[right]+nums[i]-target
                    if abs(diff)<abs(closet_sum):
                        closet_sum=diff
                    if diff==0:
                        return target
                    elif diff<0:
                        left+=1
                    else:
                        right-=1
         return closet_sum+target
                    
                    
  
if __name__ == "__main__":
    print Solution().threeSumClosest([-1, 0, 1, 2, -1, -4], 5)      
