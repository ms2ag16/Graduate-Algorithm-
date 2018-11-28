# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, 0)

    def dfs(self, root, preSum):
        if root is None:
            return 0
        preSum = preSum * 10 + root.val
        if root.left == None and root.right == None:
            return preSum

        return self.dfs(root.left, preSum) + self.dfs(root.right, preSum)