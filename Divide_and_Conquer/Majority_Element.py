def majorityEleHelper(nums,left,right):

    if left==right:
        return nums[left]

    mid = (left + right) / 2


    Majority_Left=majorityEleHelper(nums,left,mid)

    Majority_Right=majorityEleHelper(nums,mid+1,right)


    if Majority_Left==Majority_Right:
        return Majority_Left

    left_count=0
    right_count=0
    for i in range (left,right+1):
        if nums[i]==Majority_Left:
            left_count+=1
    for j in range(left,right+1):
        if nums[j]==Majority_Right:
            right_count+=1

    return Majority_Left if left_count>right_count else Majority_Right

if __name__=="__main__":
    A=[3,3,4]
    print majorityEleHelper(A,0,len(A)-1)
