class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res=[]
        import math
        numset=[i for i in range(1,n+1)]
        k=k-1
        while len(numset)>1:
            n=n-1
            index=k/math.factorial(n)
            res.append(str(numset[index]))
            k=k%math.factorial(n)
            numset.remove(numset[index])
        res.append(str(numset[0]))
        res="".join(res)
        return res

