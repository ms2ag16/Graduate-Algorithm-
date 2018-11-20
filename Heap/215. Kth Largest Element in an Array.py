class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        return heapq.nlargest(k,nums)[-1]


if __name__=="__main__":
    print (Solution().findKthLargest([3,2,3,1,2,4,5,5,6],4
))