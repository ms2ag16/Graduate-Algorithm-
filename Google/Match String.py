"""
Given two strings, such as str="BABA", str2="CAB". 
The goal is to from str1 by concatenating multiple copies of str2, before concatenating a copy of str2, 
you can remove any number of chars from it.
1. Is it possbile to form str1, given str2?
2. What is the minimum number of copies?
"""

def check(str1, str2):
  set1=set(str1)
  set2=set(str2)
  if len(set2)<len(set1):
    return False
  for char in set1:
    if char not in set2:
      return False
  return True

