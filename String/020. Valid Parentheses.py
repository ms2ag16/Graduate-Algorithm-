"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true
Example 2:
Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
"""
# idea: use stack, LIFO/FILO check

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        par={'(':')', '[':']', '{':'}'}
        stack=[]
        for c in s:
            if c in par:
                stack.append(c)
            elif stack and par[stack.pop()]==c:
                continue
            else:
                return False
        if not stack:
            return True
        else:
            return False
        
    def isValid2(self,s):
        # use set
        left=('(','[','{')
        right=(')','[','}')
        stack=[]
        for c in s:
            if c not in left:
                return False
            else:
                if not stack:
                    return False
                p=stack.pop()
                if left.index(p)!=right.index(c):
                    return False
        return len(stack)==0
        
       
