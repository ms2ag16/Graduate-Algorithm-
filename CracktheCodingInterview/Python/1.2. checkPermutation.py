def checkPermutation(s1, s2):
    len1, len2=len(s1),len(s2)
    if len1!=len2: return False
    if sorted(s1)!=sorted(s2): return False
    return True

if __name__=="__main__":
    assert (checkPermutation('abc ', ' abc'))==True
