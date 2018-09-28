""" time complexity: O(N^2) """
def insertionSorting(arr):
    for i in range(len(arr)):
        preIndex=i-1
        current=arr[i]
        while preIndex >=0 and arr[preIndex] > current:
            arr[preIndex +1] = arr[preIndex]
            preIndex-=1
        arr[preIndex+1] = current
    return arr
