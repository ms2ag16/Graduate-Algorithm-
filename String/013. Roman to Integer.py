
# 思路： 从后向前（从右向左）遍历str，规则是如果左边大于右边最大数，则相加，如果小就相减。 
# key1：len(s)-1, -1, -1
# key2: xrange is faster than range
"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sum=0
        maxDigit=1
        for i in xrange(len(s)-1,-1,-1):
            if digits[s[i]]>=maxDigit:
                maxDigit=digits[s[i]]
                sum+=digits[s[i]]
            else:
                sum-=digits[s[i]]
        return sum
