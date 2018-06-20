"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry=1
        for i in range(len(digits)-1, -1,-1):
            digits[i]+=carry
            if digits[i]<10:
                carry=0
                break
            else:
                digits[i]-=10

        if carry==1:
            digits.insert(0,1)

        return digits




if __name__ == "__main__":
    print  Solution().plusOne([9, 9, 9, 9])
