class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n=len(words)
        idx1, idx2= n,n
        res=n
        for i in range(n):
            if words[i]==word1:
                idx1=i
                res=min(res,abs(idx1-idx2))
            elif words[i]==word2:
                idx2=i
                res=min(res, abs(idx1-idx2))
        return res

if __name__=="__main__":
    print (Solution().shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"))