# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack=[(p,q)]
        while stack:
            left,right=stack.pop()
            if not left and not right:
                continue
            elif None in [left, right]:
                return False
            elif left.val!=right.val:
                return False
            stack.append((left.right, right.right))
            stack.append((left.left, right.left))
        return True
