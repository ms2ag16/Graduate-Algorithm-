"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
class Solution(object):
    letters={'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], 
            '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], 
            '8': ['t','u','v'], '9':['w','x','y','z']}
    def dfs(self,digits,string, res):
        if not digits:
            return res.append(string)
        else:
            for l in self.letters[digits[0]]:
                self.dfs(digits[1:], string+l, res)
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res=[]
        if not digits:
            return res
        self.dfs(digits, "", res)
        return res
        
