"""
1) Print Max element of a given list
2) Print median of a given list
3) Print the first nonrecurring element in a list
4) Print the most recurring element in a list
5) Greatest common Factor

"""
l1=[2,2,3,3,35,6,7,8,1,76,89]
print (max(l1))

"""----------------------------"""
sortedLst = sorted(lst)
lstLen = len(lst)
index = (lstLen - 1) // 2

if (lstLen % 2):
    return sortedLst[index]
else:
    return (sortedLst[index] + sortedLst[index + 1])/2.0

"""----------------------------"""


def fn(s):
  order = []
  counts = {}
  for x in s:
    if x in counts:
      counts[x] += 1
    else:
      counts[x] = 1
      order.append(x)
  for x in order:
    if counts[x] == 1:
      return x
  return None

#----------------------
def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a