"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        def dfs(candidates, target, current, res):
            if sum(current)==target:
                return res.append(current)
            if sum(current)> target:
                return
            else:
                for i, v in enumerate(candidates):
                    dfs(candidates[i:], target, current+[v], res)
        candidates.sort()
        dfs(candidates, target, [], res)
        return res
      
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates=sorted(candidates)
        res=[]
        self.dfs(candidates, target, 0, [], res)
        return  res

    def dfs(self, candidates, target, index, current, res):
        for i in range(index, len(candidates)):
            if candidates[i]==target:
                current.append(candidates[i])
                res.append(current)
                return
            if candidates[i]>target:
                return
            else:
                self.dfs(candidates, target-candidates[i], i, current+[candidates[i]], res)
                """ use i instead of i+1, since allow use multiple times of each number in candidates """




if __name__=="__main__":
    print Solution().combinationSum(candidates = [2,3,6,7], target = 7)
