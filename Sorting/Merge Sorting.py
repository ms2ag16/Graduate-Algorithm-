def merge(left, right):
    res=[]
    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    res=res+left+right
    return res

def mergeSort(lists):
    if len(lists)<=1:
        return lists
    mid=len(lists)//2
    left=mergeSort(lists[:mid])
    right=mergeSort(lists[mid:])
    return merge(left,right)
