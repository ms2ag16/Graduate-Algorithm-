"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res=defaultdict(list)
        for s in strs:
          res[tuple(sorted(s))].append(s)
        return res.value
 

class Solution2(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map={}
        for i, v in enumerate(strs):
          target="".join(sorted(v))
          if target not in map:
            map[target]=[v]
          else:
            map[target].append(v)
        res=[]
        for value in map.values():
          result+=[sorted(value)]
        return result
      
        
if __name__ == "__main__":
    assert Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['nat', 'tan'], ['bat'],
                                                                                    ['ate', 'eat', 'tea']]       
