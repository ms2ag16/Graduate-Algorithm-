"""
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
"""
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        max_len=0
        start=0
        count=defaultdict(int）
        for i in range(len(s)):
            count[s[i]]+=1
            while len(count)>2:
              count[s[start]]-=1
              if count[s[start]]==0:
                  count.pop(s[start], None)
              start+=1
            max_len=max(max_len, i-start+1)
        return max_len
            
        
        
