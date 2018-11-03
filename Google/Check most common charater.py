    def countFreq(string s):    
        from collections import defaultdict
        count=defaultdict(int)
        for i in range(len(s)):
            count[s[i]]+=1
        res=[]
        common= max(count.values())
        print common
        for ele, freq in count.items():
            if freq==common:
                res.append([ele,freq])
        return res
