"""
In elections taht use the ballot box system for voting, each voter 
"""
def electionWinner(s):
        vote=dict()
        for i in range(len(s)):
            if s[i] in vote:
                vote[s[i]]+=1
            else:
                vote[s[i]]=1
        maxIndex=sorted(vote.values(), reverse=True)[0]

        sortedS=sorted(vote.keys(), reverse=True)
        print sortedS, vote

        for i in sortedS:
            if vote[i]==maxIndex:
                return i
