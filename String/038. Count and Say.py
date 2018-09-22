"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
Note: Each term of the sequence of integers will be represented as a string.

Example 1:
Input: 1
Output: "1"
"""

# 可以递归，也可以用迭代
# 递归，递归出口 n==1, return '1'

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1: return '1'
        s=self.countAndSay(n-1)
        res=''
        count=1
        for j in range(len(s)):
            if (j+1)<len(s) and s[j]==s[j+1]:
                count+=1
            else:
                res+=str(count)
                res+=s[j]
                count=1
        return res
        
