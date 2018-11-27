class Solution(object):
    def findTargetSumWays(self, nums, S):
        from collections import defaultdict
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        _len = len(nums)
        dp = [defaultdict(int) for _ in range(_len + 1)]
        dp[0][0] = 1
        for i, num in enumerate(nums):
            for sum, cnt in dp[i].items():
                dp[i + 1][sum + num] += cnt
                dp[i + 1][sum - num] += cnt
        return dp[_len][S]





if __name__=="__main__":
    print (Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))