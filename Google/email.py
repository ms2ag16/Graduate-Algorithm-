def parseEmail(emails):
    """

    :param email: list, array
    :return: return list

    """
    n=len(emails)
    from collections import defaultdict
    count=defaultdict(int)
    res=[]

    for email in emails:
        local,domain=email.split('@')
        local=''.join(local.split('.'))
        locals=local.split('+')
        if len(locals)>1:
            local=locals[0]
        email=local+'@'+domain
        count[email]+=1

    for k,v in count.items():
        if v>1:
            res.append(k)
    return res


if __name__=="__main__":
     print parseEmail(["ab+work@example.com","a.b@example.com","dupli....cate@example.com","d.up.l.i.c.a.t.e@example.com"])
