exam1=[['A','B'], ['B','C'], ['A','C'], ['B','D'], ['E']]
from collections import defaultdict
counts=defaultdict(int)
for relation in exam1:
    print(relation)
    for people in relation:
        if len(relation)>1:
            counts[people]+=1
        else:
            counts[people]=0

print(counts)


