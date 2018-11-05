""" iteration version """
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        stack = [(root, sum-root.val, [root.val])]
        while stack:
            curr, val, ls = stack.pop()
            if not curr.left and not curr.right and val == 0:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, val-curr.right.val, ls+[curr.right.val]))
            if curr.left:
                stack.append((curr.left, val-curr.left.val, ls+[curr.left.val]))
        return res 



""" recursion version """
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res=[]
        self.dfs(root, sum, [root.val], res)
        return res
    
    def dfs(self, root, sum, path,res):
        
        if not root:
            return 
        if sum==root.val and not root.left and not root.right:
            res.append(path)
        sum-=root.val
        if root.right:
            self.dfs(root.right, sum, path+[root.right.val], res)
        if root.left:
            self.dfs(root.left, sum, path+[root.left.val],res)
