"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""

""" using DFS, loop over string, and check it's substring one by one """

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not string:
            return[]
        res=[]
        self.dfs(s, [], res)
        return res
    
    def isPalindrome(self,s):
        for i in range(len(s)):
            if s[i] != s[len(s)-1-i]: return False
        return True
        
    def dfs(self,s, curr_list,res):
        if len(s) == 0: 
            res.append(curr_list)
        for i in range(1, len(s)+1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], curr_list+[s[:i]], res)
                
