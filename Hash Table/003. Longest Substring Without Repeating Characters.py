"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", which the length is 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """ DP concept"""
        start=maxlength=0
        usedChar={}
        for i in range(len(s)):
            if s[i] in usedChar and start <=usedChar[s[i]]:
                start=usedChar[s[i]]+1
            else:
                maxlength=max(maxlength, i-start+1)

            usedChar[s[i]]=i

        return maxlength

 if __name__=="__main__":
    print Solution().lengthOfLongestSubstring("pwwkew")
       
