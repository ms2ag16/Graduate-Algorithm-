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
# 用 回溯 backtracking，
# 思路是 类似穷举，穷举 考虑用回溯
# 条件有2个： 1. left不能超过n， 否则无效；2. left不能超过right
# 穷举的时候，先是一直➕（，直到n，然后if left<n不满足，继续向下执行 right<left

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # backtracking
        res=[]
        def dfs(res, S,left,right):
            if len(S)==2*n:
                res.append(S)
                return
            if left<n:
                dfs(res,S+'(',left+1,right)
            if right<left:
                dfs(res, S+')', left,right+1)
        dfs(res,'',0,0)
        return res
