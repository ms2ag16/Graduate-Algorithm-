"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""

# 思路就是取strs中第一个str，然后逐个字符进行比较，遇到不等或是其中一个str结尾，即跳出遍历循环，返回prefix
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        prefix=""
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i>= len(strs[j]) or strs[0][i]!=strs[j][i]:
                    return prefix
            prefix+=strs[0][i]
        return prefix
                
