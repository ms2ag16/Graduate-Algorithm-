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
        
       
