def findLevels(predator):
    pmap=dict()
    cur=[]
    for i in range(len(predator)):
        if predator[i]==-1:
            cur.append(i)
        else:
            if predator[i] not in pmap:
                pmap[predator[i]]=[i]
            else:
                pmap[predator[i]].append(i)
    length=0
    while len(cur)>0:
        length+=1
        new=[]
        for c in cur:
            if c in pmap:
                new+=pmap[c]
        cur=new
    return length

print findLevels([1,-1,3,1])
