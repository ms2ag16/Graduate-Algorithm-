"""O(nlogn)"""
def Max_profit(data,left,right):
    if left >= right:
        return 0
    mid=int((left+right)/2)

    """ recursively call Max_profit on Left/Right side"""
    LeftMaxProfit=Max_profit(data,left,mid)
    RightMaxProfit=Max_profit(data,mid+1,right)

    """ calculate on the third senario: lowest in left, highest in right"""
    if (left<mid<right):
        lowest=min(data[left:mid+1])
        highest=max(data[mid+1:right+1])
    else:
        lowest=highest=data[mid]


    return LeftMaxProfit,RightMaxProfit,highest-lowest

"""O(n)"""
def Max_profit2(data,left,right):
    if left >= right:
        return (0,data[left],data[right])

    mid=int((left+right)/2)
    highest=lowest=data[mid]

    """ recursively call Max_profit on Left/Right side"""
    LeftMaxProfit, highestLeft, lowestLeft=Max_profit2(data,left,mid)

    RightMaxProfit, highestRight, lowestRight=Max_profit2(data,mid+1,right)

    """ calculate on the third senario: lowest in left, highest in right"""
    max_Profit=max(LeftMaxProfit, RightMaxProfit,highestRight-lowestLeft)


    return max_Profit, max(highest,highestRight,highestLeft),min(lowest,lowestLeft,lowestRight)


if __name__=="__main__":
    price=[2,9,5,-3,8,9,-2]
    n=len(price)-1
    print Max_profit(price,0,n)
    print Max_profit2(price,0,n)
