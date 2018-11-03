import random

def generate(self, s):
    for pro in s.values():
        pro*=10
    check=[]
    for ele,freq in s.items():
        while freq>0:
            check.append(ele)
            freq-=1
    index=random.randint(0,len(check))
    return check[index], s[check[index]]
