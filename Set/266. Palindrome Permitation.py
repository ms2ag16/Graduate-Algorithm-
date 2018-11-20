"""
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false

Example 2:

Input: "aab"
Output: true
"""

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        seen = set()
        for letter in s:
            if letter not in seen:
                seen.add(letter)
            else:
                seen.remove(letter)

        return len(seen) <= 1

