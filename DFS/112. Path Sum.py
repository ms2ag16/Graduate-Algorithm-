# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.dfs(root, sum)

    def dfs(self, root, sum):
        if not root:
            return False
        sum-=root.val
        if not root.left and not root.right:
            return sum==0
        return self.dfs(root.left, sum) or self.dfs(root.right, sum)