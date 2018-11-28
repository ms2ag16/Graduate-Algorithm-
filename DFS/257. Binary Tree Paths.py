"""
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res = []
        self.dfs(root, str(root.val), res)
        return res

    def dfs(self, root, path, res):
        if not root.left and not root.right:
            return res.append(path)
        if root.left:
            self.dfs(root.left, path + '->' + str(root.left.val), res)
        if root.right:
            self.dfs(root.right, path + '->' + str(root.right.val), res)