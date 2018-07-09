"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique
combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
"""
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        if not candidates:
            return []
        candidates.sort()
        result=[]
        self.dfs(candidates, target, [], result)
        return result
    
    def dfs (self, candidates, target, current, result):
        s=sum(current) if current else 0
        if s> target:
            return
        elif s==target:
            result.append(current)
            return
        else:
            i=0
            while i < len(candidates):
                self.dfs(candidates[i+1:], target, current+[candidates[i]], result)
                while i+1 < len(candidates) and candidates[i+1]==candidates[i]:
                    i+=1
                i+=1
                
