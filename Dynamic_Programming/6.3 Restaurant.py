
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
