def minSubarray(input):
    if input is None or len(input)==0:
        return 0
    freq={}
    lens={}
    for i in range(len(input)):
        k=input[i]
        if k not in freq:
            freq[k]=1
            lens[k]=[i,i]
            print lens[k]
        else:
            lens[k][1]=i
            print lens[k][1]
            freq[k]+=1

    max_freq=max(freq.values())
    min_len=len(input)
    for k ,v in freq.items():
        if v==max_freq:
            min_len=min(lens[k][1] - lens[k][0]+1, min_len)
    return min_len

s=[1,2,2,3,2]
print minSubarray(s)
