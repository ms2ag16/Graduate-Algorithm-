"""
mplement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
Example 1:

Input: "42"
Output: 42
Example 2:

Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
"""
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()

        # check valid str and length
        if not str or len(str) == 0:
            return 0
        # check first sign belong to +/-
        flag = 1
        if str[0] in ['+', '-']:
            if str[0] == '-':
                flag = -1
            str = str[1:]

        # check if str is digit or string
        if not str or not str[0].isdigit():
            return 0

        # start check regular string with first character is digit
        res = 0
        for c in str:
            if not c.isdigit():
                break
            res = res * 10 + ord(c) - ord('0')

        res = flag * res

        res = res if res <= 2147483647 else 2147483647
        res = res if res >= -2147483648 else -2147483648
        return res


if __name__=="__main__":
    print Solution().myAtoi("+67546")


"""  首先去除字符串前缀空格；
    然后判断有无正负号，若有正负号，设置正负号标志，指针后移一位，否则，不做处理；
    判断第一个字符是否是数字，若不是，说明是无效数字，返回为0 ；否则正常处理；这个过程指针不移动；
    循环处理后面的字符；若是数字字符，正常处理，并判断是否越界；若不是数字字符，退出循环，返回数字"""
        
