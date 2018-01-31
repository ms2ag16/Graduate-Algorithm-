def Quick_Sort(data):
    if len(data)<=1:
        return data

    left=[]
    right=[]
    pivot=data.pop()

    for i in data:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)
    return Quick_Sort(left)+[pivot]+Quick_Sort(right)

if __name__=="__main__":
    A=[3,7,8,5,2,1,9,5,4]
    print Quick_Sort(A)
