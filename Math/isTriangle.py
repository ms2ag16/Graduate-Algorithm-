def isTriangle(a,b,c):
    res=[]
    if a is None or len(a)==0:
        return res
    n=len(a)
    for i in range(n):
        s=sorted([a[i],b[i],c[i]])
        print s
        if s[0]+s[1]>s[2]:
            res.append(True)
        else:
            res.append(False)
    return res

print isTriangle([3,4,7],[4,8,9],[5,13,13])
