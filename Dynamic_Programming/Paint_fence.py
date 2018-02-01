""" There is a fence with n posts, each post can be painted with one of the k colors."""
""" You have to paint all the posts such that no more than two adjacent fence posts have the same color."""
""" Return the total number of ways you can paint the fence."""
def Paint_fence(n,k):
    if n ==0:
        return 0
    if n==1:
        return k

    same=diff=[0 * i for i in range(n+1)]

    same[2]=k
    diff[2]=k*(k-1)
    for i in range(3,n+1):
        same[i]=diff[i-1]
        diff[i]=same[i-1]*(k-1)+ diff[i-1]*(k-1)


    return diff[n]+same[n]






if __name__=="__main__":
    print Paint_fence(5,2)
