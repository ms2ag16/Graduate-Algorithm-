"""
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Example 1:

Input: buf = "abc", n = 4
Output: "abc"
Explanation: The actual number of characters read is 3, which is "abc".
Example 2:

Input: buf = "abcde", n = 5 
Output: "abcde"
"""
# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        """ read4(buf), buf is the destination buffer"""
        idx=0
        while n>0:
            buf4=[""]*4             """         ["","","",""]         """
            l4=read4(buf4)
            if not l4:
                return idx
            for i in range(min(l4,n)):
                buf[idx]=buf4[i]
                idx+=1
                n-=1
        return idx
               
               
        
