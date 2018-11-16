"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
"""
""" BFS, go over each element in the string and to see if till now is a word in dict, if it is then add the left part into the queue"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        queue=[s]
        visited=set([s])
        while queue:
            front =queue.pop(0)
            if front in wordDict:
                return True
            prefix=""
            for c in front:
                prefix+=c
                suffix=front[len(prefix):]
                if prefix in wordDict and suffix not in visited:
                    queue.append(suffix)
                    visited.add(suffix)
        return False
