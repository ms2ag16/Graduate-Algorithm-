"""
给一个字符串，求满足条件的substring的数量：substring有刚好K个distinct characters
Given a string of lowercase alphabets, count all possible substrings (not necessarily distinct) that has exactly k distinct characters.
Examples:

Input: abc, k = 2
Output: 2
Possible substrings are {"ab", "bc"}

Input: aba, k = 2
Output: 3
Possible substrings are {"ab", "ba", "aba"}

Input: aa, k = 1
Output: 3
Possible substrings are {"a", "a", "aa"}
"""
class Solution(object):
    def countKDist(self, string, k):
        """
        :type string: str
        :type k: int
        :rtype: int
        """
        res = 0

        strLen = len(string)

        count = [0 for _ in range(26)]

        for i in range(strLen):
            dist_count =0

            for j in range(i, strLen):
                if (count[ord(string[j]) - ord('a')] == 0):
                    dist_count+=1

                count[ord(string[j]) - ord('a')] += 1

                if (dist_count == k):
                    res +=1

        return res


if __name__=="__main__":
    paragraph = "a, a, a, b,b,b, c."
    banned =['a']
    print Solution().countKDist("abcda", 3)
