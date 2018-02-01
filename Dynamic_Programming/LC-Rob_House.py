class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        
        values=nums
        
        if len(nums)==1:
            return nums[0]
       
        for i in range(2,len(nums)):
             temp=values[i]
             for j in range(0,i-1):
                if (nums[i] + values[j])>temp:
                    temp=nums[i] + values[j]
             values[i]=max(values[i-1],temp)

        return max(values)
