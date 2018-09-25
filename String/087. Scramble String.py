"""
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".
"""
class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        """思路是： recursion 递归出口： s1==s2, return True, 递归条件，gr和rg，则是s1[0]==s2[1], 也就是说s1[part1]==s2[part2] 或者s1[part1]=s2[part1]"""
        if s1==s2:
            return True
        from collections import defaultdict
        count1=count2=defaultdict()
        for k1,k2 in zip(s1, s2):
            count1[k1]+=1
            count2[k2]+=1
        if count1!=count2:
            return False
        for i in range(1, len(s1)):
           if self.isScramble(s1[i:], s2[i:]) and self.isScramble(s1[:i],s2[:i]):
              return True
           if self.isScramble(s1[i:], s2[:len(s2)-i] and self.isScramble(s1[:i], s2[len(s2)-i:]):
              return True
        return False
            
