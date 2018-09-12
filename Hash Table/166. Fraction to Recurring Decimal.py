"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
"""


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        int_ans, dec_ans = "", ""
        hmap = {}
        idx = 0
        # positive or negative
        if numerator * denominator < 0:
            int_ans += "-"
        print "int_ans=%s"%int_ans
        numerator, denominator = abs(numerator), abs(denominator)

        mod = numerator / denominator
        reminder = numerator % denominator
        int_ans += str(mod)
        if reminder != 0:
            int_ans += "."

        while reminder > 0:
            mod = reminder * 10 / denominator
            if reminder not in hmap:
                dec_ans += str(mod)
                hmap[reminder] = idx
                idx += 1
            else:
                i = hmap[reminder]
                dec_ans = dec_ans[:i] + "(" + dec_ans[i:] + ")"
                break

            reminder = reminder * 10 % denominator
        return int_ans + dec_ans




if __name__=="__main__":
    print Solution().fractionToDecimal(1, 13)
