# 6.3. Yuckdonald's is considering opening a series of restaurants along Quaint Valley Highway (QVH).
# The n possible locations are along a straight line, and the distances of these locations from the
# start of QVH are, in miles and in increasing order,m1;m2; : : : ;mn. The constraints are as follows:
#  At each location, Yuckdonald's may open at most one restaurant. The expected profit from
# opening a restaurant at location i is pi, where pi > 0 and i = 1; 2; : : : ; n.
#  Any two restaurants should be at least k miles apart, where k is a positive integer.
# Give an effcient algorithm to compute the maximum expected total profit subject to the given
# constraints.


def open_res(locations, profit,k):
    num_res=len(locations)
    P=[]

    for i in range(num_res):
        P.append(0)

    for i in range(1,num_res):
        temp_max=profit[i]
        for j in range(0,i):
            if locations[i]-locations[j]>=k:
                if profit[i]+P[j]>=temp_max:
                    temp_max=profit[i]+P[j]
            else:
                if temp_max<=P[i-1]:
                    temp_max=P[i-1]
        P[i]=temp_max

    return P


if __name__=='__main__':
    profits=[0,5,7,8,9]
    locati=[0,4,7,9,10]
    k=5
    print open_res(locati,profits,k)

 
