def longestPalindrome(s):
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
