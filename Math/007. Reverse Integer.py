"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev=0
        flag=1
        if x<0:
            flag=-1
        x=abs(x)
        while (x!=0):
            pop=x%10
            x/=10
            rev=rev*10 + pop
        rev*=flag
        if  rev> 2147483647 or rev<-2147483648:
            return 0
        return rev

if __name__ == "__main__":
    print Solution().reverse(-431)
        
        
