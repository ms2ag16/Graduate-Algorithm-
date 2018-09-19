"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
""" 

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # 其实最终输出 按行输出就好！ 那么只需要判断 到达row【numRow-1】需要换方向scan character。判断标准currentLine%（numRow-1）==0
        # ！=0 currentLine+1； ==0， currentLine-1，回到上一行，接着写，即换方向
        curLine=0
        step=-1
        n=len(s)
        if(numRows>=n) or numRows<=1:
            return s
        res=['']*numRows
        for c in s:
            if curLine%(numRows-1)==0:
                step=-step
            res[curLine]+=c  # string can +=, cannot append
            curLine+=step
        return ''.join(res) # format  '.join(iterable)
