class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import defaultdict
        import heapq
        res=[]
        count=defaultdict(int)
        for num in nums:
            count[num]+=1
        sorted_count=sorted(count.items(),key=lambda kv:kv[1],reverse=True)
        for i in range(k):
            res.append(sorted_count[i][0])
        print (res)


if __name__=="__main__":
    print (Solution().topKFrequent([1,1,1,2,2,2,3,4,5,6,6],2))