class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = nums
        for i in range(1, len(nums)):
            sum[i] = max(nums[i], sum[i - 1] + nums[i])

        return max(sum)




if __name__=="__main__":
    test=[8,3,-5,6,9,-10,1,2]
    A=Solution()
    print (A.maxSubArray(test))
