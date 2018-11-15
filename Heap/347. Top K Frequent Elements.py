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

""" using heap"""
class Solution1(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import heapq
        from collections import defaultdict
        count=defaultdict(int)
        heap, res = [], []
        for num in nums:
            count[num]+=1
        for key, value in count.items():
            entry=[value,key]
            heapq.heappush(heap,entry)
        for i in heapq.nlargest(k,heap):
            res.append(i[1])
        return sorted(res)




if __name__=="__main__":
    print (Solution1().topKFrequent([1,1,1,2,2,2,3,4,5,6,6],2))