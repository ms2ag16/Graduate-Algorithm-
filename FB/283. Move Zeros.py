class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = 0  # records the position of "0"
        for i in range(len(nums)):
            if nums[i] != 0:
                print ('nums now =',nums)
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
        return nums


if __name__=="__main__":
    print (Solution().moveZeroes([-1,0,1,2,-1,-4]))