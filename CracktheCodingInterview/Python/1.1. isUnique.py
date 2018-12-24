def isUnique(s):
    if len(s)<=0: return None
    flag=0
    for i in range(len(s)):
        val=ord(s[i])-ord('a')
        if((flag & (1<<val))>0):
            return False
        flag |= (1<<val)
        print flag
    return True

if __name__=="__main__":
    print isUnique('abcdb')
