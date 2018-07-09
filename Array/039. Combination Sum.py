"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in 
candidates where the candidate numbers sums to target.
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
        if not candidates:
            return []
        candidates.sort()
        result=[]
        self.dfs(candidates, target, [], result)
        return result
    
    def dfs(self, candidates, target, cur_num, result):
        s=sum(cur_num) if current else 0
        if s >target:
            return
        elif s==target:
            result.append(cur_num)
        else:
            for i, v in enumerate (candidates):
                 """ because no duplicate combination, so only add the element after candidates[i]"""
                self.dfs(candidates[i:], target, cur_num+[v], result)
                
     def dfs2(self,candidates, target, start, valuelist,result):
        length=len(candidates)
        if target==0:
          return result.append(valuelist)
        for i in range(start,length):
            if target< candidates[i]:
                return
            self.dfs(candidates, target-candidates[i], i, valuelist+[candidates[i]]
 
     
if __name__ == "__main__":
    print Solution().combinationSum([2, 3, 6, 7], 7)
 
 
        
