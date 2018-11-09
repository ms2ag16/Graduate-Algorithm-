""" Iteration 
    use pointer to solve the problem.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        if not root:
            return
        stack=[root]
        pointer=TreeNode(0)
        while stack:
            top=stack.pop()
            if not top:
                continue
            stack.append(top.right)
            stack.append(top.left)
            pointer.right=top
            pointer.left=None
            pointer=top
            
