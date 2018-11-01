# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root)
        
    
    def dfs(self, root):
        if not root:
            return 0
        if root.left is None:
            return self.dfs(root.right)+1
        if root.right is None:
            return self.dfs(root.left)+1
        return min(self.dfs(root.left), self.dfs(root.right))+1
