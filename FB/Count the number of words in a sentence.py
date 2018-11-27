def count(sentence):
    import string
    sentence="".join(char for char in sentence if char not in string.punctuation)
    words=sentence.split(' ')
    counts=dict()
    for word in words:
        if word  in counts:
            counts[word]+=1
        counts[word]=1
    return counts

if __name__=="__main__":
    print (count('I have a big apple.'))
