def check(self, s):
        l=[1 for i in s]
        res=[]
        word=set()
        for i in range(1, len(s)):
            if s[i]==s[i-1]:
                l[i]=l[i-1]+1
            if l[i]>=2:
                word.add(s[i])
        print word
        for e in word:
            start=s.index(e)
            end=len(s)-s[::-1].index(e)-1
            res.append([start, end])
        return res








if __name__=='__main__':
    print Solution().check('biiirrrd')
