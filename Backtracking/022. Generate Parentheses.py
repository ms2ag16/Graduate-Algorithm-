"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(left, right, string, res):
            if left==n and right==n:
                return res.append(string)  
            
            if left<n:
                generate(left+1, right, string+"(", res)
            if left>right:
                generate(left, right+1, string+")", res)
        res=[]
        generate(0,0,"", res)
        return res
        
