class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        count=defaultdict(int)
        start=0
        max_len=0
        for i in range(len(s)):
            count[s[i]]+=1
            while len(count)>k:
                count[s[start]]-=1
                if count[s[start]]==0:
                    count.pop(s[start],None)
                start+=1
                
            max_len=max(max_len, i-start+1)
        return max_len
