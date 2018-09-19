"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
"""

class Solution(object):
    def longestPalindrome_wrong method(self, s):
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

        return trans_s, maxl """ trans后求最长common substring 的方法是有问题的，caabdaac, 对与本身有对称的case trans后，caa和caa common， 但不是回字文"""
    

if __name__=="__main__":
    print Solution().longestPalindrome("babad")
