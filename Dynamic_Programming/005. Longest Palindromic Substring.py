def longestPalindrome(s):
    """ 
    基本思路是对任意字符串，如果头和尾相同，
    那么它的最长回文子串一定是去头去尾之后的部分的最长回文子串加上头和尾。
    如果头和尾不同，那么它的最长回文子串是去头的部分的最长回文子串和去尾的部分的最长回文子串的较长的那一个。 
    """
    n=len(s)
    maxl=0
    start=0
    for i in range(n):
        if i-maxl>=1 and s[i-maxl-1:i+1]==s[i-maxl-1:i+1][::-1]:
            start=i-maxl-1
            maxl+=2
            continue
        if i-maxl>=0 and s[i-maxl:i+1]==s[i-maxl:i+1][::-1]:
            start=i-maxl
            maxl+=1
    return s[start:start+maxl]


if __name__=='__main__':
    s="dacad"
    print longestPalindrome(s)
