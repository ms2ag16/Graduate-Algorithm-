"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        if len(s)==len(t)==0:
            return True
        anagram=dict()
        for l in s:
            if l not in anagram:
                anagram[l]=1
            else:
                anagram[l]+=1
        for l in t:
            if l not in anagram:
                return False
            else:
                anagram[l]-=1
        for i in anagram.keys():
            if anagram[i]==0:
                return True
            else:
                return False
