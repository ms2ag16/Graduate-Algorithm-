""" string common operation:
     string.ascii_letters
        The concatenation of the ascii_lowercase and ascii_uppercase constants
     string.ascii_lowercase
     string.ascii_uppercase

     string.digits

     string.hexdigits
        The string '0123456789abcdefABCDEF'

     string.octdigits
        The string '01234567'

     string.punctuation
         String of ASCII characters which are considered punctuation characters in the C locale.

     string.whitespace
        A string containing all characters that are considered whitespace.
        On most systems this includes the characters space, tab, linefeed, return, formfeed,
        and vertical tab.
"""

def avgLength( s):
    import string

    s="".join(char for char in s if char not in string.punctuation)
    words=s.split(' ')
    length=0
    counts=0
    for word in words:
        length+=len(word)
        counts+=1
    return length/counts

if __name__=="__main__":
    print (avgLength('I have a big apple.'))