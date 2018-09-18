"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        trans_s=s[::-1]
        res=[[ 0 for i in range(n)] for i in range(n)]
        for i in range(n):
                res[0][i]=1 if s[i]==trans_s[0] else 0
                res[i][0]=1 if s[0]==trans_s[i] else 0
        maxl=0
        print res
        for i in range(1,n):
            for j in range(1,n):
                if trans_s[i]==s[j]:
                    res[i][j]=1+res[i-1][j-1]
                    maxl=max(res[i][j], maxl)
                else:
                    res[i][j]=0

        return trans_s, maxl

if __name__=="__main__":
    print Solution().longestPalindrome("babad")
