def findHoles(nums):
    holes=[1,0,0,0,1,0,1,0,2,1]
    res=[]
    if nums is None or len(nums)==0:
        return res
    
    for i in range(len(nums)):
        num=nums[i]
        count=0
        if num==0:
            count=1
        else:
            while num!=0:
                count+=holes[num%10]
                num/=10
        res.append(count)

    return res

print findHoles([123])
